import json
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "demo"))
from preview import analyze


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "demo" / "synthetic_case.json"
        cls.packets = json.loads(path.read_text())["packets"]

    def test_synthetic_protocol_counts(self):
        result = analyze(self.packets)
        self.assertEqual(result["protocols"], {"ARP": 2, "DNS": 1, "TCP": 4, "UDP": 1})

    def test_evidence_references_existing_packets(self):
        result = analyze(self.packets)
        ids = {p["id"] for p in self.packets}
        self.assertEqual(len(result["findings"]), 2)
        for finding in result["findings"]:
            self.assertTrue(set(finding["packet_ids"]) <= ids)
            self.assertEqual(finding["certainty"], "unverified heuristic")

    def test_no_evidence_no_findings(self):
        self.assertEqual(analyze([])["findings"], [])

    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            analyze([self.packets[0], self.packets[0]])


if __name__ == "__main__":
    unittest.main()
