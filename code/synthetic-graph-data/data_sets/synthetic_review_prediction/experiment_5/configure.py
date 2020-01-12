from ..meta_classes import DataSetProperties
from ..meta_classes.data_set_properties import PersonStyleWeightDistribution, PersonStyleWeight, ProductStyleWeight
from ..utils import WeightedOption, Distribution
from ..classes import PersonStylePreferenceEnum, ProductStyleEnum, Style
from ..experiment_1.opinion_function import opinion_function
from .style_functions import product_style_function, person_style_function
from graph_io.classes.dataset_name import DatasetName

def create_data_set_properties(DATASET_NAME:DatasetName, N_STYLES) -> DataSetProperties:
    styles = [Style(str(i)) for i in range(N_STYLES)]

    for style in styles:
        ProductStyleEnum.register('LIKES_'+style.value, style)
        PersonStylePreferenceEnum.register('HAS_'+style.value, style)

    n_products = 50
    reviews_per_product = 200

    data_set_properties = DataSetProperties(
        dataset_name=DATASET_NAME,
        n_reviews=n_products * reviews_per_product,
        n_companies=0,
        reviews_per_product=reviews_per_product,
        reviews_per_person_distribution=[
            WeightedOption[int](20, 1)
        ],
        person_styles_distribution=PersonStyleWeightDistribution([
            PersonStyleWeight(x, 1) for x in PersonStylePreferenceEnum.iterate()
        ]),
        product_styles_distribution=Distribution[ProductStyleWeight, ProductStyleEnum]([
            ProductStyleWeight(x, 1) for x in ProductStyleEnum.iterate()
        ]),
        person_company_number_of_relationships_distribution=[],
        opinion_function=opinion_function,
        person_style_function=person_style_function,
        product_style_function=product_style_function
    )

    return data_set_properties
