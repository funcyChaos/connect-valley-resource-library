$(document).on('googleMapPointFieldWidget:placeChanged', function(e, placeObj, lat, lng, wrapElemSelector, djangoInput){
	let streetAddress 											= ""
	const wrapper = document.querySelector(wrapElemSelector)
	const row = wrapper.closest('.form-row, .inline-related')
	placeObj.address_components.forEach(component=>{
		if(component.types.includes("street_number")){
			streetAddress	+= component.long_name
			streetAddress	+= " "
		}else if(component.types.includes("route")){
			streetAddress	+= component.long_name
		}else if(component.types.includes("locality")){
			row.querySelector('[name$="city"]').value = component.long_name
		}else if(component.types.includes("administrative_area_level_1")){
			row.querySelector('[name$="state"]').value = component.long_name
		}else if(component.types.includes("postal_code")){
			row.querySelector('[name$="zip_code"]').value = component.long_name
		}
	})
	row.querySelector('[name$="street_address"]').value = streetAddress
})