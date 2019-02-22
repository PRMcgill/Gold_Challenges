
import claim

claims = []


class RepoFunctions:

    def add_claim(self, claim_id, claim_type, description, claim_amount,
                  date_of_incident, date_of_claim, is_valid):
        nc = claim.Claims(claim_id, claim_type, description,
                          claim_amount, date_of_incident,
                          date_of_claim, is_valid)
        claims.append(nc)

    def see_claims(self):
        return claims

    def take_next_claim(self):
        claims.pop(0)
