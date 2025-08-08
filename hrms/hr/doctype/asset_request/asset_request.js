// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Asset Request", {
	refresh(frm) {
        frm.set_query("asset_item", () => {
            return {
                filters: {
                    custodian: ""
                }
            };
        });
        if (frm.doc.workflow_state === 'Pending Procurement Action') {
            frm.add_custom_button(__('Create Asset'), () => {
                frappe.set_route('Form', 'Asset','new-asset');
            });
          }
	},
});


