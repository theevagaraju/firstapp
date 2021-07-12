# -*- coding: utf-8 -*-
# Copyright (c) 2021, raju and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
#import frappe
from frappe.model.document import Document

class FirstappCourse(Document):
	def validate (self) :
		total_course = len(frappe.get_all("Firstapp Course"))	
		frappe.db.set_value("Firstapp Setting",None,"total_course", total_course)
		frappe.db.commit()