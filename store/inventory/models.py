import re
from django.db import models
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
from uuslug import slugify

def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
				   slug_separator='-'):
	"""
	Calculates and stores a unique slug of ``value`` for an instance.

	``slug_field_name`` should be a string matching the name of the field to
	store the slug in (and the field to check against for uniqueness).

	``queryset`` usually doesn't need to be explicitly provided - it'll default
	to using the ``.all()`` queryset from the model's default manager.
	"""
	slug_field = instance._meta.get_field(slug_field_name)

	slug = getattr(instance, slug_field.attname)
	slug_len = slug_field.max_length

	# Sort out the initial slug, limiting its length if necessary.
	slug = slugify(value)
	if slug_len:
		slug = slug[:slug_len]
	slug = _slug_strip(slug, slug_separator)
	original_slug = slug

	# Create the queryset if one wasn't explicitly provided and exclude the
	# current instance from the queryset.
	if queryset is None:
		queryset = instance.__class__._default_manager.all()
	if instance.pk:
		queryset = queryset.exclude(pk=instance.pk)

	# Find a unique slug. If one matches, at '-2' to the end and try again
	# (then '-3', etc).
	next = 2
	while not slug or queryset.filter(**{slug_field_name: slug}):
		slug = original_slug
		end = '%s%s' % (slug_separator, next)
		if slug_len and len(slug) + len(end) > slug_len:
			slug = slug[:slug_len-len(end)]
			slug = _slug_strip(slug, slug_separator)
		slug = '%s%s' % (slug, end)
		next += 1

	setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
	"""
	Cleans up a slug by removing slug separator characters that occur at the
	beginning or end of a slug.

	If an alternate separator is used, it will also replace any instances of
	the default '-' separator with the new separator.
	"""
	separator = separator or ''
	if separator == '-' or not separator:
		re_sep = '-'
	else:
		re_sep = '(?:-|%s)' % re.escape(separator)
	# Remove multiple instances and if an alternate separator is provided,
	# replace the default '-' separator.
	if separator != re_sep:
		value = re.sub('%s+' % re_sep, separator, value)
	# Remove separator from the beginning and end of the slug.
	if separator:
		if separator != '-':
			re_sep = re.escape(separator)
		value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
	return value
	

# Create your models here.


class Category( models.Model ):
	name = models.CharField( verbose_name="Category", max_length = 50, unique=True)
	slug = models.CharField( verbose_name="Category Slug", max_length = 50, unique=True)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
		
	def __unicode__(self):
		return _(u'%s') % (self.name)

	def save(self, **kwargs):
		if not self.id:
			unique_slugify(self, self.name)
		super(Category, self).save()


class SubCategory( models.Model ):
	category = models.ForeignKey(Category, verbose_name="Category", null=True)
	name = models.CharField( verbose_name="Sub-Category", max_length = 50, unique=True)
	slug = models.CharField( verbose_name="Sub-Category Slug", max_length = 50, unique=True)

	class Meta:
		verbose_name = "Sub-Category"
		verbose_name_plural = "Sub-Categories"
		
	def __unicode__(self):
		return _(u'%s') % (self.name)

	def save(self, **kwargs):
		if not self.id:
			unique_slugify(self, self.name)
		super(SubCategory, self).save()


class Brand( models.Model ):
	name = models.CharField( verbose_name="Brand", max_length = 50, unique=True)
	slug = models.CharField( verbose_name="Brand Slug", max_length = 50, unique=True)

	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brands"
		
	def __unicode__(self):
		return _(u'%s') % (self.name)

	def save(self, **kwargs):
		if not self.id:
			unique_slugify(self, self.name)
		super(Brand, self).save()


class Item( models.Model ):
	tags = TaggableManager()
	status = models.BooleanField('Status', default=True)
	category = models.ForeignKey(Category, verbose_name="Category")
	sub_category = models.ForeignKey(SubCategory, verbose_name="Sub-Category", null=True)
	brand = models.ForeignKey(Brand, verbose_name="Brand", null=True)
	name = models.CharField( verbose_name="Item", max_length = 100 )
	description = models.CharField( verbose_name="Description", max_length = 150)
	price = models.DecimalField( verbose_name="Price", max_digits=8, decimal_places=2)
	slug = models.CharField( verbose_name="Item Slug", max_length = 100, unique=True)
	image = models.ImageField( verbose_name="Item Image", upload_to='items/', null=True, blank=True)
	
	class Meta:
		verbose_name = "Item"
		verbose_name_plural = "Items"
		
	def __unicode__(self):
		return _(u'%s') % (self.name)

	def save(self, **kwargs):
		if not self.id:
			unique_slugify(self, self.name)
		super(Item, self).save()


class FrequentItem( models.Model ):
	main_item = models.ForeignKey(Item, verbose_name="Main Item")
	frequent_item = models.ForeignKey(Item, related_name="frequent_item", verbose_name="Frequent Item")
	support = models.PositiveIntegerField( verbose_name="Min Support", default=0)
	