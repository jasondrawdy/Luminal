# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Luminal
# Author: Jason Drawdy
# Version: 1.0.0
# Date: 07/07/23
# #########################################################################
# Description:
# This module is responsible for all property base classes within Luminal.
# #########################################################################
from typing import Optional, Type

class ClassProperty(property): # pragma: no cover
    """
    A decorator that turns a method into a class property.

    This class inherits from Python's built-in :class:`property` class and overrides\
    its :func:`__get__()` method to allow it to be used as a class property.

    Examples
    ----------
    To use :class:`ClassProperty`, simply decorate a method with it:

    >>> class MyClass:
    ...     _prop = 'value'
    ...
    ...     @ClassProperty
    ...     def prop(cls):
    ...         return cls._prop
    ...
    >>> MyClass.prop
    'value'
    """
    def __get__(self: "ClassProperty", *args: tuple, **_) -> object:
        """
        Get the value of the class property for a given object or class.

        Returns
        ----------
        :class:`object`
            The value of the class property.

        Raises
        ----------
        AttributeError
            If the property is accessed on an object that does not
            have an attribute with the same name as the property.
        """
        return super(ClassProperty, self).__get__(args[1])

    def __set__(self: "ClassProperty", cls_or_instance: object, value: object) -> None:
        """
        Set the value of the class property.

        This method is called when the class property is set on the class or an
        instance of the class. However, because this is a class property, this
        method will only be called when the property is set by the class itself,
        and is not intended for external use; or even by private methods.

        Parameters
        ----------
        cls_or_instance : :class:`object`
            The class that the property is being set on.
        value : :class:`object`
            The new value of the class property.

        Raises
        ----------
        AttributeError 
            When attempting to set the class property on an
            instance of the class rather than the class itself.
        """
        # Call this method only on the class, not the instance.
        super(ClassProperty, self).__set__(self._get_class(cls_or_instance), value)

    def __delete__(self: "ClassProperty", cls_or_instance: object) -> None:
        """
        Delete the class property from the class.

        Parameters
        ----------
        cls_or_instance : :class:`object`
            The class from which the class property is being deleted.

        Raises
        ----------
        AttributeError
            When attempting to delete the class property from an
            instance of the class rather than the class itself.
        """
        # Call this method only on the class, not the instance.
        super(ClassProperty, self).__delete__(self._get_class(cls_or_instance))

    def _get_class(self: "ClassProperty", cls_or_instance: Type[object|type]) -> type:
        """
        Get the class of an object, or return the class itself if given.

        Parameters
        ----------
        cls_instance : :class:`Type[object|type]`
            The object or type whose class should be retrieved.

        Returns
        ----------
        :class:`type`
            The class of the object if one is provided, or the class itself if a
            class is provided.

        Raises:
        ----------
        TypeError 
            An exception if ``cls_or_instance`` is not a valid object or type.
        """
        if isinstance(cls_or_instance, type):
            return cls_or_instance
        else:
            return type(cls_or_instance)
        

class MetaProperties(type): # pragma: no cover
    """
    A metaclass that enables the `ClassProperty` decorator to work properly
    with class-level operations like setting and deleting properties.

    When using `ClassProperty` to create class properties, the containing class
    must use this metaclass in order for the property to work properly with
    class-level operations like setting and deleting the property.

    For example, to use `ClassProperty` to define a read-only class property:

    >>> class MyClass(metaclass=MetaProperties):
    ...     @ClassProperty
    ...     def prop(cls):
    ...         return "value"
    ...
    >>> MyClass.prop # Get the value of the property.
    'value'
    >>> MyClass.prop = "new value" # Attempt to set the value of the property.
    AttributeError: can't set attribute
    >>> del MyClass.prop # Attempt to delete the property.
    AttributeError: can't delete attribute

    Note that attempting to set or delete a `ClassProperty` object will raise
    an :class:`AttributeError` by default, unless the :func:`__set__()` and/or 
    :func:`__delete__()` methods are defined on the :class:`ClassProperty` object.

    See Also
    ----------
    :class:`ClassProperty`
        The decorator used to create class properties.
    """
    def __setattr__(self: "MetaProperties", name: str, value: object) -> None:
        """
        Override the :func:`__setattr__()` method to allow setting class properties.

        This method is called when an attribute of the class is set. If the\
        attribute is a :class:`ClassProperty` instance (as determined by the\
        presence of a :func:`__set__()` method on the instance), it will call\
        the :func:`__set__()` method to set the property's value. Otherwise, it\
        will invoke the superclass implementation of :func:`__setattr__()` to handle\
        the attribute in the usual way.

        Parameters
        ----------
        name : :class:`str`
            The name of the attribute that's being set.
        value : :class:`object` 
            The new value of the attribute.

        Raises
        ----------
        AttributeError
            If ``name`` refers to a :class:`ClassProperty` object and the :func:`__set__()`\
            method of that object raises an :class:`AttributeError`.
        """
        attribute: Optional[ClassProperty] = self._get_attribute(name)
        if attribute:
            attribute.__set__(self, value)
        else:
            super(MetaProperties, self).__setattr__(name, value)

    def __delattr__(self: "MetaProperties", name: str):
        """
        Override the :func:`__delattr__()` method to allow deleting of class properties.

        Parameters
        ----------
        name : :class:`str` 
            The name of the attribute that's being deleted.

        Raises
        ----------
        AttributeError
            If ``name`` refers to a :class:`ClassProperty` object and the :func:`__delete__()`\
            method of that object raises an :class:`AttributeError`.

        Notes
        ----------
        - This method is called when an attribute of the class is deleted. If the\
        attribute is a :class:`ClassProperty` instance (as determined by the presence\
        of a :func:`__delete__()` method on the instance), it will call the :func:`__delete__()`\
        method to delete the property. Otherwise, it will invoke the superclass implementation of\
        :func:`__delattr__()` to handle the attribute in the usual way.
        
        """
        attribute: Optional[ClassProperty] = self._get_attribute(name)
        if attribute:
            attribute.__delete__(self)
        else:
            super(MetaProperties, self).__delattr__(name)

    def _get_attribute(self: "MetaProperties", name: str) -> Optional[ClassProperty]:
        """
        Retrieves a :class:`ClassProperty` attribute with the given ``name`` from this :class:`MetaProperties` instance.

        Parameters
        ----------
        name : :class:`str`
            The name of the attribute to retrieve.

        Returns
        ----------
        Optional[:class:`ClassProperty`]
            The :class:`ClassProperty` object for the attribute, if it exists. Otherwise, returns ``None``.
        """
        if (name in self.__dict__ and isinstance(self.__dict__[name], ClassProperty)):
            return self.__dict__[name]
        else:
            return None