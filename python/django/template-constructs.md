# Django template language constructs

The syntax of the Django template language involves *four* constructs.

## Variables

A variable outputs a value from the context, which is a dict-like object mapping keys to values.

```
My first name is {{ first_name }}. My last name is {{ last_name }}.
{{ my_list.0 }}
```

## Tags

Tags provide arbitrary logic in the rendering process.

```
{% csrf_token %}
Hello{% if user.is_authenticated %}, {{ user.username }}.{% endif %}
```

## Filters

Filters transform the values of variables and tag arguments.

```
{{ django|title }}
{{ my_date|date:"Y-m-d" }}
```

## Comments

```
{# this won't be rendered #}
```
