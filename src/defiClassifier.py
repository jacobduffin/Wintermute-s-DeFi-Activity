import requests
import re

class DeFiProtocolClassifier:

    NON_DEFI = {"cex", "cefi"}

    def __init__(self):
        # Load DeFiLlama protocol data
        self.protocols = requests.get("https://api.llama.fi/protocols").json()

        # Pre-process all protocols once
        for p in self.protocols:
            p["domain"] = self._get_domain(p.get("url"))
            p["gecko"] = (p.get("gecko_id") or "").lower()

            p["name_norm"] = self._normalise(p["name"])
            p["domain_norm"] = self._normalise(p["domain"])
            p["gecko_norm"] = self._normalise(p["gecko"])


    # Helper functions

    def _get_domain(self, url):
        if not url:
            return ""
        domain = re.sub(r"https?://(www\.)?", "", url).split("/")[0]
        return domain.lower()

    def _normalise(self, x):
        return re.sub(r"[^a-z0-9]+", " ", x.lower()).strip()


    # Classification Logic

    def _classify_protocol(self, proto):
        if proto is None:
            return "Unknown"

        category = (proto.get("category") or "").lower()
        parent = (proto.get("parentProtocol") or "").lower()

        if category in self.NON_DEFI:
            return "Non-DeFi"
        if "cex" in parent or "cefi" in parent:
            return "Non-DeFi"

        return "DeFi"


    # Scoring Logic

    def _score_match(self, cp, proto):
        cp_norm = self._normalise(cp)
        cp_tokens = cp_norm.split()

        score = 0

        fields = {
            "name": proto["name_norm"],
            "domain": proto["domain_norm"],
            "gecko": proto["gecko_norm"],
        }

        # Token matching
        for token in cp_tokens:
            for field_text in fields.values():

                field_tokens = field_text.split()

                # Exact token match
                if token in field_tokens:
                    score += 10

                # Partial token match
                elif any(token in ft for ft in field_tokens):
                    score += 3

        # Exact normalised full match
        for field_text in fields.values():
            if cp_norm == field_text:
                score += 30

        # Penalty for length mismatch
        score -= abs(len(proto["name_norm"]) - len(cp_norm)) * 0.5

        return score


    # Diagnose Method

    def diagnose(self, counterparties):
        """
        Takes a list/Series of counterparties and returns structured match results.
        """
        results = []

        for cp in counterparties:
            cp_clean = cp.strip()

            best = None
            best_score = -1

            # Find best protocol match
            for p in self.protocols:
                s = self._score_match(cp_clean, p)
                if s > best_score:
                    best = p
                    best_score = s

            # Threshold check
            if best_score < 10:
                results.append({
                    "input": cp_clean,
                    "match": "Unknown",
                    "score": best_score,
                    "classification": "Unknown"
                })
            else:
                results.append({
                    "input": cp_clean,
                    "match": best["name"],
                    "score": best_score,
                    "classification": self._classify_protocol(best)
                })

        return results
