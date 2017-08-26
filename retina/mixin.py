# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

class MenuContextDataMixin(object):

    menu = None

    def get_context_data(self, **kwargs):
        context = super(MenuContextDataMixin, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': self.get_menu()
            }
        )
        return context

    def get_menu(self):
        """
        Override this method to customize the menu_entry.
        """
        menu = self.menu
        if not menu:
            raise ImproperlyConfigured(
                'Define {0}.menu '
                '{0}.get_menu().'.format(self.__class__.__name__))
        
        return menu
