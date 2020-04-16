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
                        title='Основное',
                        models=(
                            'appmain.models.ProjectConfig',
                            'appmain.models.Feedback',
                        )
                    ),
                    modules.ModelList(
                        title='Каталог',
                        models=(
                            'appcatalogs.models.Category',
                            'appcatalogs.models.Product',
                            'appcatalogs.models.Brand',
                            'appcatalogs.models.VolumeDesignation',
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