import parse_utils

class QuerySeveral:

    def __init__(self, wikifile):
        """ constructor """
        # TODO: Fill in!


    def process_page(self, wiki_page:str):
        """
        reads one wiki/xml file, processes each page, populating the
        dictionary that maps words->page_id->frequency counts
        
        Parameters:
        wiki_page -- the path to an xml file with pages (each with title, 
                     id, and text sections)
        """

        # TODO: Fill in!
        

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
        
        # TODO: Fill in!
        

