import { createResource } from "frappe-ui"
import { employeeResource } from "./employee"

const transformEmployeeCertificateRequests = (data) => {
    return data.map((request) => {
        request.doctype = "Employee Certificate"
        return request
    })
}

export const myEmployeeCertificateRequests = createResource({
    url: "hrms.api.employee_certificate.get_employee_certificate_requests",
    params: {
        employee: employeeResource.data.name,
        limit: 10,
    },
    auto: true,
    cache: "hrms:my_employee_certificate_requests",
    transform(data) {
        return transformEmployeeCertificateRequests(data)
    },
})
