# -*- coding: utf-8 -*-
# Copyright (c) 2021, raju and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe
from frappe.model.document import Document

class FirstappStudent(Document):
	def validate (self) : # keyword for default
		total_student = len(frappe.get_all("Firstapp Student"))
		frappe.db.set_value("Firstapp Setting",None,"total_student", total_student)
		frappe.db.commit()
