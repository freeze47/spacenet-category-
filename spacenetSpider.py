import scrapy


class SpacenetProduct(scrapy.Spider):
    name = 'spacenet'
    start_urls = ['https://spacenet.tn']

    def parse(self, response):

        categories = response.css('div.sp-vermegamenu  ul  li.item-1.vertical-cat.parent')

        for category in categories:
            mainCategory = category.css('a::attr(title)').get()
            subCategories = category.css('div.dropdown-menu ul li.item-2.col-lg-3.cat-child.parent')

            for subCat in subCategories:
                mainSubCat = subCat.css('a::attr(title)').get()
                otherCat = subCat.css('div.dropdown-menu ul li.item-3 span::text')
                others = []

                for other in otherCat:

                    others.append(other.get())

                cleaned_others = [other.replace(' ', '') for other in others]
                cleanedOthers = [other.replace('\n', '') for other in cleaned_others]

                keys = [i for i in range(1, len(cleanedOthers) + 1)]

                yield {
                    "main category": mainCategory,
                    "SubCat": mainSubCat,
                    "last categories": dict(zip(keys, cleanedOthers)),
                }
