from django import template

register = template.Library()

@register.filter(name='find_language')
def find_language(sites_data, lang):
    return [site for site in sites_data if site.Language == lang]

@register.filter(name='find_country')
def find_countrye(sites_data, cntry):
    return [site for site in sites_data if site.Country == cntry]