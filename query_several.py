import parse_utils

class QuerySeveral:
    word_freq_dict = {} # the dictionary of words to dict of ids to counts
    id_title_dict = {}  # the dictionary of ids to titles

    
    def __init__(self, wikifile):
        parse_utils.parse(wikifile, self.process_page)


    def process_page(self, wiki_page:str):
        """
        reads one wiki/xml file, processes each page, populating the
        dictionary that maps words->page_id->frequency counts
        
        parameters:
            wiki_page   the path to an xml file with pages (each with title, 
                        id, and text sections)
        """
        
        page_id = int(wiki_page.find("id").text)
        page_title = wiki_page.find("title").text.strip()
        page_text = wiki_page.find("text").text.strip()
        if wiki_page.find("text").text is None: page_text = ""
        
        self.id_title_dict[page_id] = page_title

        tokens = parse_utils.get_tokens(page_title + " " + page_text)
        
        for word in tokens:
            if parse_utils.word_is_link(word):
                # split link into the text and the destination, but only process the text
                # TODO: Fill in!

                # include link text because it's part of the page text
                
                # TODO: Fill in!
                pass # Placeholder statement (remove this)
            else:
                # for non-links, just record its presence
                
                # TODO: Fill in!
                pass # Placeholder statement (remove this)
        

    def query(self, search_term:str, format="title") -> list:
        """
        searches for page titles that contain the search term

        Parameters:
        search_term -- the string to search for in wiki pages; for this
                       assignment these can be just single words

        format -- used to control whether a list of page ids or titles 
                  is returned. title is the default, but the value can
                  be set to "id" when query is called to get the page 
                  ids instead (ids might be less error-prone to check in tests)
        
        Returns:
        the list of pages that contain the search term (as per the format)
        """
        if format not in ["id", "title"]:
            raise ValueError("Invalid results format " + format)
        
        term_low = search_term.lower()
        if term_low in parse_utils.STOP_WORDS:
            print("WARNING: STOP WORD isn't indexed -- " + search_term)
            return []

        term_low = parse_utils.stem_and_stop(term_low)
        if term_low in self.word_freq_dict:
            # if the term is in the dictionary, get the list of ids and sort it
            # TODO: Fill in!

            # If our query is for ids, just return the sorted list of ids
            if format=="id": 
                # TODO: Fill in!
                pass
            # If our query is for titles, convert the sorted list of ids to titles
            elif format=="title": 
                # TODO: Fill in!
                pass
            
        else: # term not in dictionary
            return []
        

