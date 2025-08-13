// Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Certificate", {
    refresh (frm) {
        console.log("onloadedd .. ")
        frm.add_custom_button(__('Print Certificate'), async function () {
            if (!frm.doc.name) {
                frappe.msgprint('Please save the document before printing.');
                return;
            }

            try {
                // 1. Get HR Settings with child table
                const hr_settings = await frappe.db.get_doc("HR Settings","HR Settings");
                console.log("hr_settings .. ", hr_settings);

                // 2. Try to find the mapping row for this certificate's purpose
                let mapping = null;
                if (hr_settings.purpose_print_format_mapping && hr_settings.purpose_print_format_mapping.length) {
                    mapping = hr_settings.purpose_print_format_mapping.find(
                        row => row.purpose === frm.doc.purpose
                    );
                }

                // 3. Determine print format from mapping, else fallback
                const print_format = mapping?.print_format || "Standard";
                const letterhead = hr_settings?.certificate_letterhead || ""; // Optional: if you add letterhead in mapping

                // 4. Build the PDF download URL
                const url = `/api/method/frappe.utils.print_format.download_pdf`
                    + `?doctype=${encodeURIComponent(frm.doc.doctype)}`
                    + `&name=${encodeURIComponent(frm.doc.name)}`
                    + `&format=${encodeURIComponent(print_format)}`
                    + `&letterhead=${encodeURIComponent(letterhead)}`
                    + `&no_letterhead=0`;

                // 5. Open in new tab
                window.open(url, '_blank');

            } catch (e) {
                console.error(e);
                frappe.msgprint(__('Unable to fetch HR Settings or mapping.'));
            }
        });
    },
});
