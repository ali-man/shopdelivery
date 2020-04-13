from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.children.append(
            modules.Group(
                title='Main',
                display='tabs',
                children=[
                    modules.ModelList(
                        title='Блог',
                        models=(
                            'appblog.models.Rubric',
                            'appblog.models.Tag',
                            'appblog.models.Article',
                        )
                    ),
                    modules.ModelList(
                        title='Каталог',
                        models=(
                            'appcatalogs.models.Category',
                            'appcatalogs.models.Product',
                        )
                    ),
                    modules.ModelList(
                        title='Блог',
                        models=(
                            'apps.general.models.CategoryArticle',
                            'apps.general.models.Article',
                        )
                    ),
                    modules.ModelList(
                        title='Статические страницы',
                        models=(
                            'apps.general.models.Slider',
                            'apps.general.models.FeedBack',
                            'django.contrib.flatpages.*',
                            # 'django.contrib.sites.*',
                        ),
                    ),
                ]
            )
        )