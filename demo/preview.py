"""BLACKBOX public preview: deterministic heuristics on synthetic metadata only.

Not a PCAP parser, AI agent or production intrusion detection system.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def analyze(packets):
    """Return protocol counts and evidence-linked *leads*, never attack verdicts."""
    ids = [p["id"] for p in packets]
    if len(ids) != len(set(ids)):
        raise ValueError("Packet IDs must be unique")
    protocols = dict(sorted(Counter(p["protocol"].upper() for p in packets).items()))
    findings = []
    tcp_by_pair = defaultdict(list)
    arp_by_ip = defaultdict(list)
    for p in packets:
        protocol = p["protocol"].upper()
        if protocol == "TCP" and isinstance(p.get("dst_port"), int):
            tcp_by_pair[(p["src"], p["dst"])].append(p)
        if protocol == "ARP" and p.get("claim_ip") and p.get("claim_mac"):
            arp_by_ip[p["claim_ip"]].append(p)
    for (src, dst), events in sorted(tcp_by_pair.items()):
        ordered = sorted(events, key=lambda p: p["ts"])
        for index, first in enumerate(ordered):
            window = [p for p in ordered[index:] if 0 <= p["ts"] - first["ts"] <= 2]
            ports = {p["dst_port"] for p in window}
            if len(ports) >= 4:
                evidence = [p["id"] for p in window]
                findings.append({
                    "type": "possible_port_sweep",
                    "summary": f"{src} contacted {len(ports)} TCP ports on {dst} in 2 seconds",
                    "packet_ids": evidence,
                    "certainty": "unverified heuristic",
                    "alternative": "Authorized scanning or administrative testing",
                })
                break
    for ip, events in sorted(arp_by_ip.items()):
        macs = {p["claim_mac"].lower() for p in events}
        if len(macs) >= 2:
            findings.append({
                "type": "arp_identity_inconsistency",
                "summary": f"Multiple MAC addresses claimed {ip}",
                "packet_ids": [p["id"] for p in events],
                "certainty": "unverified heuristic",
                "alternative": "Failover, virtualized hosts or legitimate reconfiguration",
            })
    return {"total_packets": len(packets), "protocols": protocols, "findings": findings}


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("synthetic_case.json")
    data = json.loads(source.read_text(encoding="utf-8"))
    result = analyze(data["packets"])
    print(json.dumps({"case": data["case_name"], **result}, indent=2))


if __name__ == "__main__":
    main()
