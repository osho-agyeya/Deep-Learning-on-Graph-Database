
# TODO: create a decorator to do this for us
from .article_0 import runner as article_0_runner
from .article_1 import runner as article_1_runner
from .experiment_1 import runner as experiment_1_runner
from .experiment_2 import runner as experiment_2_runner
from .experiment_3 import runner as experiment_3_runner
from .experiment_4 import runner as experiment_4_runner
from .experiment_5 import runner as experiment_5_runner

runner = dict()
runner.update(article_0_runner)
runner.update(article_1_runner)
runner.update(experiment_1_runner)
runner.update(experiment_2_runner)
runner.update(experiment_3_runner)
runner.update(experiment_4_runner)
runner.update(experiment_5_runner)

from .experiment_1 import DATASET_NAME as EXPERIMENT_1_DATASET
from .experiment_2 import DATASET_NAME as EXPERIMENT_2_DATASET
from .experiment_3 import DATASET_NAME as EXPERIMENT_3_DATASET
from .experiment_4 import DATASET_NAME as EXPERIMENT_4_DATASET
from .article_0    import DATASET_NAME as ARTICLE_0_DATASET
from .article_1    import DATASET_NAME as ARTICLE_1_DATASET




