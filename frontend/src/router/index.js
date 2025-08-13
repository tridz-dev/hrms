import { createRouter, createWebHistory } from "@ionic/vue-router"

import TabbedView from "@/views/TabbedView.vue"
import attendanceRoutes from "./attendance"
import leaveRoutes from "./leaves"
import claimRoutes from "./claims"
import employeeAdvanceRoutes from "./advances"
import salarySlipRoutes from "./salary_slips"

const routes = [
	{
		path: "/",
		redirect: "/home",
	},
	{
		path: "/",
		component: TabbedView,
		children: [
			{
				path: "",
				redirect: "/home",
			},
			{
				path: "/home",
				name: "Home",
				component: () => import("@/views/Home.vue"),
			},
			{
				path: "/dashboard/attendance",
				name: "AttendanceDashboard",
				component: () => import("@/views/attendance/Dashboard.vue"),
			},
			{
				path: "/dashboard/leaves",
				name: "LeavesDashboard",
				component: () => import("@/views/leave/Dashboard.vue"),
			},
			{
				path: "/dashboard/expense-claims",
				name: "ExpenseClaimsDashboard",
				component: () => import("@/views/expense_claim/Dashboard.vue"),
			},
			{
				path: "/dashboard/salary-slips",
				name: "SalarySlipsDashboard",
				component: () => import("@/views/salary_slip/Dashboard.vue"),
			},
		],
	},
	{
		path: "/login",
		name: "Login",
		component: () => import("@/views/Login.vue"),
	},
	{
		path: "/profile",
		name: "Profile",
		component: () => import("@/views/Profile.vue"),
	},
	{
		path: "/notifications",
		name: "Notifications",
		component: () => import("@/views/Notifications.vue"),
	},
	{
		path: "/settings",
		name: "Settings",
		component: () => import("@/views/AppSettings.vue"),
	},
	{
		path: "/resignation-dashboard",
		name: "ResignationDashboard",
		component: () => import("@/views/ResignationDashboard.vue"),
	},
	{
		path: "/resignation-list",
		name: "ResignationApplicationListView",
		component: () => import("@/views/ResignationApplicationList.vue"),
	},
	{
		path: "/resignation-form/:id?",
		name: "ResignationApplicationFormView",
		component: () => import("@/views/ResignationApplication.vue"),
		props: true,
	},
	{
		path: "/employee-resignation/:id?",
		name: "EmployeeResignationDetailView",
		component: () => import("@/views/ResignationApplication.vue"),
		props: true,
	},
	{
		path: "/employee-resignation-form/:id?",
		name: "EmployeeResignationFormView",
		component: () => import("@/views/ResignationApplication.vue"),
		props: true,
	},
	{
		path: "/asset-request-dashboard",
		name: "AssetRequestDashboard",
		component: () => import("@/views/AssetRequestDashboard.vue"),
	},
  {
    path: "/leave-resumption-dashboard",
    name: "LeaveResumptionDashboard",
    component: () => import("@/views/LeaveResumptionDashboard.vue"),
  },
  {
    path: "/employee-certificate-dashboard",
    name: "EmployeeCertificateDashboard",
    component: () => import("@/views/EmployeeCertificateDashboard.vue"),
  },
	{
		path: "/asset-request-list",
		name: "AssetRequestListView",
		component: () => import("@/views/AssetRequestApplicationList.vue"),
	},
  {
    path: "/leave-resumption-list",
    name: "LeaveResumptionListView",
    component: () => import("@/views/LeaveResumptionApplicationList.vue"),
  },
  {
    path: "/employee-certificate-list",
    name: "EmployeeCertificateListView",
    component: () => import("@/views/EmployeeCertificateApplicationList.vue"),
  },
	{
		path: "/asset-request-form/:id?",
		name: "AssetRequestFormView",
		component: () => import("@/views/AssetRequestApplication.vue"),
		props: true,
	},
  {
    path: "/leave-resumption-form/:id?",
    name: "LeaveResumptionFormView",
    component: () => import("@/views/LeaveResumptionApplication.vue"),
    props: true,
  },
  {
    path: "/leave-resumption/:id?",
    name: "LeaveResumptionDetailView",
    component: () => import("@/views/LeaveResumptionApplication.vue"),
    props: true,
  },
  {
    path: "/employee-certificate-form/:id?",
    name: "EmployeeCertificateFormView",
    component: () => import("@/views/EmployeeCertificateApplication.vue"),
    props: true,
  },
  {
    path: "/employee-certificate/:id?",
    name: "EmployeeCertificateDetailView",
    component: () => import("@/views/EmployeeCertificateApplication.vue"),
    props: true,
  },
	{
		path: "/asset-request/:id?",
		name: "AssetRequestDetailView",
		component: () => import("@/views/AssetRequestApplication.vue"),
		props: true,
	},
	{
		path: "/invalid-employee",
		name: "InvalidEmployee",
		component: () => import("@/views/InvalidEmployee.vue"),
	},
	...attendanceRoutes,
	...leaveRoutes,
	...claimRoutes,
	...employeeAdvanceRoutes,
	...salarySlipRoutes,
]

const router = createRouter({
	history: createWebHistory("/hrms"),
	routes,
})

export default router
