class RawPageDao:

    '''
    Provides interface to persistent RawPage storage
    '''

    def __init__(self, **config):

        '''
        Setup an instance of RawPageDao
        :param **config: Configuration passed to implementation
        '''
        pass

    def storePage(self, rawPageData):

        '''
        Stores the given RawPageData object into
        persistent storage.
        Returns None on success, otherwise a string containing
        an error message.
        '''
        pass
