# class HeatmapService(object):
#     def __init__(self,
#                  timeout=TIMEOUT,
#                  retries=RETRIES):
#
#         assert(timeout >= 0)
#         self.timeout = timeout or self.TIMEOUT
#
#         assert(isinstance(retries, int) and retries >= 0)
#         self.retries = retries or self.RETRIES
#
#     def search_gene(self, gene_name):