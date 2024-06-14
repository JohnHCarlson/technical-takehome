import re

def anonymize_names_parta(text: str):
    """
    Anonymizes names in the given text by replacing them with 'ANON'. Assume names are capitalized, and no other words are.

    Examples:
        anonymize_names_parta("Alice and Bob are talking to Charlie.") 
        -> "ANON and ANON are talking to ANON."
        
        anonymize_names_parta("Alice, Bob, and Charlie went to the park.") 
        -> "ANON, ANON, and ANON went to the park."
        
        anonymize_names_parta("Dr. Alice visited Prof. Bob at the university.") 
        -> "ANON ANON visited ANON ANON at the university."

    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.



    Test cases:

        "John is writing this test for the Senate Appropriations Committee" 
        -> "ANON is writing this test for the ANON ANON ANON" 

        "John went to get lunch with peter, Kevin, and Tim in NYC."
        -> "ANON went to get lunch with peter, ANON, and ANON."

        "Peter was upset that John did not correctly anonymize him in the above example. He also was about edge case of capitalization of words that are not proper nouns, like at the beginning of a sentence."
        -> "ANON was upset that ANON did not correctly anonymize him in the above example. ANON also was about edge case of capitalization of words that are not proper nouns, like at the beginning of a sentence."
    """
    
    pattern = r'\b[A-Z].*?\b'    
    anonymized_text = re.sub(pattern, "ANON", text)
    return anonymized_text
   
   
 
def anonymize_names_partb(text: str):
    """
    Anonymizes names in the given text by replacing them with 'ANON'. Names can take any shape or form.
 
    Examples: (Note: Examples not provided as implementation depends on heuristics)
 
    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.
    """

    """
    The first decision I would make here is (at least for a first draft implementation) to implement the same rule about capitalization. We can't always assume proper grammar but proper nouns are a great place to start even without the guarantee.
    For now I kept the answer to this, though my next steps for improvement are below.

    The next heuristic I would come to is to consult some sort of a list of names. I haven't done a problem like this before but there might be an API, or have some sort of local list. This brings some immediate issues with time to solve though.

    While I am less familiar with machine learning algorithms we are in a great time for natural language processing, using some of these tools to help identify names and other information we want to anonymize is another great way, and will likely be 
    better for speed.
    """
    
    pattern = r'\b[A-Z].*?\b'    
    anonymized_text = re.sub(pattern, "ANON", text)
    return anonymized_text
    

 
 
if __name__ == '__main__':
    # Example usage
    parta_input_text = "Alice and Bob are talking to Charlie."
    print("Part A")
    print(f"{parta_input_text} -> {anonymize_names_parta(parta_input_text)}")
    print()


    # Example strings- you can add more test strings. No expectation that these all
    # pass!
    partb_test_strings = [
        "Alice and Bob are talking to Charlie about going to New York City.",
        "alice and bob are discussing with Charlie about visiting Los Angeles.",
        "Bob and Eve are planning a trip to paris next summer.",
        "Charlie and Alice met with Dave in San Francisco last week.",
        "eve and Charlie were excited about the event in Chicago.",
        "Charlie and Bob are thinking of moving to Tokyo soon.",
        "Alice and Dave went to see a show in London.",
        "Alice and Bob had dinner with Eve in Madrid.",
        "bob and Eve are going to Sydney for a conference.",
        "Charlie and Alice took a vacation in Rome.",
        "Charlie and Dave are considering a job offer in Berlin.",
        "eve and Charlie are visiting their friend in Amsterdam.",
        "Charlie and Bob are attending a wedding in Bangkok.",
        "Alice and Dave spent their holidays in Barcelona.",
        "Bob and Eve are looking for apartments in Vienna.",
        "Charlie and Dave are organizing an event in Prague.",
        "alice and Charlie are exploring opportunities in Dubai.",
        "Bob and Charlie are discussing their plans in Dublin.",
        "Alice and Bob are thinking about a trip to Vancouver.",
        "Charlie and Eve are preparing for a move to Montreal."
    ]
    print("Part B")
    for input_text in partb_test_strings:
        print(f"{input_text} -> {anonymize_names_partb(input_text)}")