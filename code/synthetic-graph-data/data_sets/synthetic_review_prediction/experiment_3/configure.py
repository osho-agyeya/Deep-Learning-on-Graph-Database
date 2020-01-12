from ..meta_classes import DataSetProperties
from ..meta_classes.data_set_properties import PersonStyleWeightDistribution, PersonStyleWeight, ProductStyleWeight
from ..utils import WeightedOption, Distribution
from ..classes import PersonStylePreferenceEnum, ProductStyleEnum, Style
from graph_io.classes.dataset_name import DatasetName

DATASET_NAME = DatasetName('synthetic_review_prediction_experiment_3')

def create_data_set_properties() -> DataSetProperties:
    N_STYLES = 6
    styles = [Style(str(i)) for i in range(N_STYLES)]

    for style in styles:
        ProductStyleEnum.register('LIKES_'+style.value, style)
        PersonStylePreferenceEnum.register('HAS_'+style.value, style)

    data_set_properties = DataSetProperties(
        n_reviews=12000,
        n_companies=100,
        reviews_per_product=75,
        reviews_per_person_distribution=[
            WeightedOption[int](1, 0.5),
            WeightedOption[int](2, 0.5)
        ],
        person_styles_distribution=PersonStyleWeightDistribution([
            PersonStyleWeight(x, 1) for x in PersonStylePreferenceEnum.iterate()
        ]),
        product_styles_distribution=Distribution[ProductStyleWeight, ProductStyleEnum]([
            ProductStyleWeight(x, 1) for x in ProductStyleEnum.iterate()
        ]),
        person_company_number_of_relationships_distribution=Distribution[ProductStyleWeight, ProductStyleEnum]([
            WeightedOption[int](i, 1) for i in range(5) # equal probability of having opinion on 0-10 companies.
            # #TODO what is the probability that someone will have an opinion on a company whose product they have actualy reviewed?
            # We can also query cypher to find ^ out in our data set!
        ])
    )

    return data_set_properties
