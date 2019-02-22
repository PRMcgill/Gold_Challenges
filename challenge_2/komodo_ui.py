
import repo

while True:
    print("Komodo Claims Department")
    user_input = input('Choose an item from the menu: \n'
                       '1. See all claims. \n'
                       '2. Enter new claim. \n'
                       '3. Take care of next claim. \n'
                       '4. Exit. \n')

    if user_input == '1':
        claims_list = repo.RepoFunctions()
        claims_list.see_claims()
        print('Claim id\t\tType\t\tDescription\t\tAmount\t\tDate of Incident\t\tDate of Claim\t\tIs Valid')
        for ind_claims in repo.claims:
            print(f'{ind_claims.claim_id}\t\t\t{ind_claims.claim_type}\t\t{ind_claims.description}\t\t{ind_claims.claim_amount}\t\t{ind_claims.date_of_incident}\t\t\t{ind_claims.date_of_claim}\t\t\t\t{ind_claims.is_valid}')

    if user_input == '2':
        claim_id = input("What is the claim id: \n")
        claim_type = input("What is type of claim is it: \n")
        description = input("Describe the claim: \n")
        claim_amount = input("What is the claim amount: \n")
        date_of_incident = input(
            "When did the incident happen:(mm/dd/yyyy) \n")
        date_of_claim = input("When was the claim issued: (mm/dd/yyyy) \n")
        is_valid = input("Is the claim valid: \n")
        new_claim = repo.RepoFunctions()
        new_claim.add_claim(claim_id, claim_type, description,
                            claim_amount, date_of_incident, date_of_claim, is_valid)
    if user_input == '3':
        next_claim = repo.claims[0]
        print("Here are the claim details for the next claim:")
        print(f'Claim ID: {next_claim.claim_id}')
        print(f'Claim Type: {next_claim.claim_type}')
        print(f'Description: {next_claim.description}')
        print(f'Claim Amount: {next_claim.claim_amount}')
        print(f'Date of Incident: {next_claim.date_of_incident}')
        print(f'Date of Claim: {next_claim.date_of_claim}')
        print(f'Is Valid: {next_claim.is_valid}')
        y_or_n = input('Do you want to deal with this claim now(y/n)?')
        if y_or_n == 'y':
            y_option = repo.RepoFunctions()
            y_option.take_next_claim()
        elif y_or_n == 'n':
            pass
    if user_input == '4':
        exit()
