class RawPageSource:

    '''
    Provides continouus stream of RawPageData objects
    '''

    def __init__(self, config):

        '''
        Setup an instance of RawPageSource
        :param **config: Configuration passed to implementation
        '''
        pass

    def getPage(self):

        '''
        Get a RawPageData object.
        '''
        pass
#
#    def markAsProcessed(id):
#
#        '''
#        Marks consumed RawPageData objects up until and including
#        the one specified through the given ID as processed and
#        propagates this information further upstream.
#        '''
#        pass
