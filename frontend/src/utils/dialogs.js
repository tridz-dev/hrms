import { alertController, toastController } from "@ionic/vue"

export const showErrorAlert = async (message) => {
	const alert = await alertController.create({
		header: "Error",
		message,
		buttons: ["OK"],
	})

	await alert.present()
}

export const showSuccessAlert = async (message) => {
	const toast = await toastController.create({
		message,
		duration: 3000,
		position: 'top',
		color: 'success',
		buttons: [
			{
				text: 'OK',
				role: 'cancel'
			}
		]
	})

	await toast.present()
}
