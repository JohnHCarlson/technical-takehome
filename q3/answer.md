Part A:

Question A(i)

SELECT requests.request_id 
FROM requests
INNER JOIN senators ON requests.senator_id=senators.senator_id
WHERE party="Democrat" 

Question A(ii)

Part B:

B1: So the immediate thought that comes to mind for me is a fairly straightforward relational database, likely one that is referenced from the main table (for example, `requests` from the above question).

B2: The basic design I am going for is a secondary table that will have a PK `duplicate_key`, an id for the original request `original_request`, and an id for the duplicate request `duplicate_request`. (For example, both Senators Murphy and Blumenthal
    submit a request to build a new bridge in Hartford. Senator Murphy submits on 03/01 and Blumenthal on 03/05. There would be two entries, both pointing to the Murphy original request, and one `duplicate_request` each pointing to each
    entry in the `requests` table._ I would also modify the `requests` table to have a `duplicate_id` column that allows for reference to this new secondary table.

B3: I know my answer in B2 is not perfect, the question doesn't really allow for the idea of an "original" request and I know that Senators (for good reason) wouldn't love that idea either. But what it does give is an ability
    to tie requests back to each other in a relational format. My first idea was a bit more basic, and was just having the duplicates table be a list of each request that was marked duplicate with some ID tying them together, but
    I found this to be more complicated than necessary. In the end I think having each duplicate request as it's own item gives us the easiest way to go back and forth between both tables.