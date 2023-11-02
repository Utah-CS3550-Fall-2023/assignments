Study Guide
===========

This document lists vocabulary, concepts, and syntax that you're
expected to know for the midterm and final.

Networking
----------

You should know rough orders of magnitude for how many websites there
are and how many internet users there are. You should know how old the
internet and the web are (to within the decade). You should be able to
explain the difference between the internet and the web. You should be
able to list the most common web browsers.

You should be able to define clients, servers, the client-server
architecture, message-passing, requests, and responses.

The parts of a URL: the protocol (or scheme), hostname (or domain),
port, and path (or page). Other parts of the URL include the query and
the fragment. You must be able to correctly identify each part of a
given URL and be able to list examples of each.

You should be able to explain the relationship between hostnames (also
called domains), IP addresses, and packet routes. You should be able
to give examples of each. You should also be familiar with what kind
of information is provided by 1) DNS lookup tools; 2) IP lookup tools;
3) traceroute.

HTML
----

You should know the following common HTML elements:

- `<a>`, `<em>`, `<strong>`, `<code>`, `<time>`, `<data>`
- `<p>`, `<pre>`, `<nav>`, `<heading>`, `<footer>`, `<main>`, `<section>`
- `<ul>`, `<ol>`, `<menu>`, and `<li>`
- `<br>`, `<hr>`, `<img>`, `<video>`
- `<meta>`, `<link>`, and `<title>`
- `<form>`, `<label>`, `<input>`, and `<button>`
- `<table>`, `<thead>`, `<tfoot>`, `<tr>`, `<td>`, and `<th>`

You should also know how to write valid pages (including doctypes),
links, images, lists, forms, and tables, including required
attributes. You should also know `&lt;`, `&gt;`, `&amp;`, `&quot;`,
and how to write comments.

You should be able to look at a screenshot of a website or application
and write valid, semantically-meaningful HTML for it using standard
tags. You should also be able to look at some HTML and suggest more
semantically meaningful elements.

You should be able to define the idea of universal accessibility and
name 3-5 common disabilities that can affect someone's use of the
internet, including both permanent and temporary disabilities. You
should know how to use the `autofocus` and `tabindex` properties. You
should be able to write textual alternatives for images. You should be
able identify common accessibility problems in HTML source code.

CSS
---

You should know the following selectors:

- Tag name, ID, and class selectors
- Descendant, child, next, and sibling selectors
- The `:hover` and `:active` pseudo-selectors

You should also know how to add `class` and `id` attributes to
elements. You should be able to write selectors to select various
elements on an HTML page.

You should know the following CSS properties:

- `font-family`, `font-weight`, `font-style`, `font-size`, and
  `text-decoration`
- `color`, `background-color`, and `opacity`
- `border` (the three-value form) and its subproperties like
  `border-bottom` or `border-left-width`
- `border-radius` (the one-value form) and `box-shadow` (the
  three-value form)

You should be able to explain the cascading rule. You should be able
to explain CSS inheritance. You should be able to use CSS shorthand
properties.

You should be able to use the following types of values:

- For lengths, the `px`, `rem`, `vw`, and `vh` units
- Also for lengths, the `calc` function, including `min` and `max`
- For colors, hex colors or named colors
- For `line-height`, numeric multipliers

You should be able to use flexible box layout for complex layouts. You
should be able to identify rows and columns in a given layout. You
should be able to use the following CSS properties for flexible box
layout:

- `display`, the `flex` value
- `flex-direction`
- `width`, `flex-grow`, and `flex-shrink`
- `justify-content` and `gap`
- `height` and `align-items`
- `margin` and `padding`

The [Notes](notes.md#flex-box) have a short checklist you can follow
to build complex flex-box layouts.

You should be able to name the components of the CSS box model (width,
padding, border, margin) correctly. You should know the order of top,
right, bottom, and left in properties like `margin`. You should be
able to explain margin collapsing at a high level.

You should be able to critique a visual design on the basis of:

- Whether the design correctly represents hierarchy
- Whether the design groups items and identifies differences
- Whether the design uses appropriate metaphors
- Whether the design uses appropriate colors
- Whether the design uses an appropriate font

You should also be able to recommend changes to address your
critiques, including describing what layouts, fonts, or colors would
better match the design.

------------------------------------------------------------------------

Topics below this line are not on the midterm but are on the final.

Django
------

You should be able to explain what components of a web server are
provided by Django. You should be able to explain the roles of the
model, view, and controller in a MVC-style web application. You should
feel comfortable explaining the roles of individual files in a
standard Django project, including `settings.py`, `urls.py`,
`models.py`, `views.py`, the `migrations/` folder, the `static/`
folder, and the `templates/` folder.

You should know the following Django field types:

- `IntegerField`, `FloatField`, and `DecimalField`
- `CharField` and `TextField`
- `EmailField` and `URLField`
- `DateField` and `DateTimeField`
- `FileField` and `ImageField`

You should be able to identify which field is appropriate in various
situations, and also be able to use the `max_length`, `blank`,
`default`, and `unique` attributes.

You should be able to model complex relationships in web application
state using `ForeignKey` relationships. You should know about the
`on_delete` and `limit_choices_to` attributes on `ForeignKey` fields.

You should be able to create, save, and query Django model objects.
Specifically, you should know the following query operators:

- `filter`, `exclude`, `union`, `intersection`, and `distinct`
- `order_by` and `reverse`
- `count` and `aggregate`
- `first` and `last`
- `contains` and `exists`

You should be able to explain the "1 + N" problem and be able to use
`select_related` to fix it.

You should be able to explain migrations, when they are created, when
they are run, and what problem they solved.

You should know the `for`, `if`, `with`, and `include` Django template
blocks. You should know the following Django template filters:

- `default`
- `floatformat`, `date`, `timesince`
- `join`, `length`, `pluralize`

You should know the syntax for defining URLs, including parameterized
URLs. You should know how to use the `render` function.

You should know how to catch errors raised by queries and how to
return 404 or other error pages.

Forms
-----

You should know how to make a valid HTML form, including form
attributes, labels, input elements, input element attributes, and
button.

You should know what the `action`, `method`, and `enctype` parameters
do on forms, and be able explain the difference between the `get` and
`post` values for `method` and choose the right one for various forms.
(You are not expected to know what values to put for `enctype`, but
you are expected to know in what case you need to set a non-default
`enctype`.)

You should know the `type`, `id`, `name`, `value`, and `disabled`
attributes on input elements. You should know the following `type`s of
input elements:

- `text`, `number`, `password`, `hidden`
- `checkbox`, `radio`, `file`
- `date`, `time`, `email`, `tel`

You should also know the `<textarea>`, `<select>`, and `<option>`
elements.

You should be able to write a Django view function (controller) that
receives form data. You should know how to use the `request.GET`,
`request.POST`, and `request.FILES` dictionaries to access form data.
You should also know how to convert form data to integers or models
objects and how to handle errors during this conversion. You should
know how to redirect to another page at the successful conclusion of a
form submission.

You should know to call `save` on model objects and how to use the
`bulk_create` and `bulk_update` methods to reduce the number of
database queries.

You should be able to describe the risks associated with file uploads.

You should be able to write validator functions or `clean` methods for
models. You should be able to check model validity after edits (by
calling `full_clean`). You should know the structure of the
`message_dict` field and be able to write forms that report user errors.

You should be able to use the following input element attributes for
client-side validation:

- `required`
- `min` / `max`
- `minlength` / `maxlength`
- `pattern`
- `accept`

You should also be able to use `:valid` / `:invalid` to style HTML
forms.

Deploy
------

You should be able to explain the role of a registrar. You should know
what A and AAAA records do in DNS. You should be able to give the
price, within an order of magnitude, of a domain ($5-20/yr), an IPv4
address ($40-60), an IPv6 address ($0), inbound bandwidth ($0),
outbound traffic ($50-100/TB), and an HTTPS certificate ($0). You
should be able to explain why you need an IPv4 address.

You should be able to name the top three could providers. You should
be able to explain the difference between a "virtualized" and
"bare-metal" cloud computer. You should be able to name some key cloud
computing instance parameters, such as CPU architecture, CPU cores,
available memory, available disk, and available accelerators like
GPUs.

You should be able to explain the roles of AWS and its EC2 and Elastic
IP services. You should be give the cost, within an order of
magnitude, of the deployment you were asked to create as part of
Assignment 4 (about $9/mo). You should be able to explain the terms
"instance" and "instance type".

You should be able to define a Service Level Agreement and explain
what a "two nines" or "five nines" availability level means. You
should be able to explain the benefits of operating redundant services
in multiple regions.

You should be able describe briefly what Linux, SystemD, APT, SSH,
BASH, and JournalCtl do. You should be able to explain the role of the
gateway server and name popular gateway servers. You should be
able to explain the role of the database server and name popular
database servers.

You should be able to explain what the `DEBUG` and `ALLOWED_HOSTS`
settings in Django do and why they differ between development and
deployment.
