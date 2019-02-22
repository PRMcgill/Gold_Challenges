class Claims:

    def __init__(self, claim_id, claim_type, description, claim_amount,
                 date_of_incident, date_of_claim, is_valid):
        self.claim_id = claim_id
        self.claim_type = claim_type
        self.description = description
        self.claim_amount = claim_amount
        self.date_of_incident = date_of_incident
        self.date_of_claim = date_of_claim
        self.is_valid = is_valid
