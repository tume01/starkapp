from repositories import AffiliateRepository

class AffiliateService(object):

    """docstring for AffliateService"""

    __affiliate_repository = AffiliateRepository.AffiliateRepository()

    def create(self,insert_data):
        return self.__affiliate_repository.create(insert_data)

    def update(self,id,update_date):
        return self.__affiliate_repository.update(id,update_data)

    def delete(self,id):
        return self.__affiliate_repository.delete(id)

    def getAffiliates(self):
        return self.__affiliate_repository.all()

    def getAffiliate(self,id):
        return self.__affiliate_repository.find(id)

    def filter(self,filters):
        return self.__affiliate_repository.filter(filters)

    def getAffiliateByMember(self,member):
        filter_data={}
        filter_data['member'] = member
        return self.__affiliate_repository.filter(filter_data)[0]
