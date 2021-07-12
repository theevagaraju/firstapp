# -*- coding: utf-8 -*-
# Copyright (c) 2021, raju and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class FirstappTutor(Document):
	def after_delete (self) :
		total_tutor = len(frappe.get_all("Firstapp Tutor"))
		frappe.db.set_value("Firstapp Setting",None,"total_tutor", total_tutor)
		frappe.db.commit ()