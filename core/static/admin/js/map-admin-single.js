$(document).on('googleMapPointFieldWidget:placeChanged', function(e, placeObj, lat, lng, wrapElemSelector, djangoInput){
	let streetAddress 											= ""
	const form = djangoInput.closest('form')
	placeObj.address_components.forEach(component=>{
		if(component.types.includes("street_number")){
			streetAddress	+= component.long_name
			streetAddress	+= " "
		}else if(component.types.includes("route")){
			streetAddress	+= component.long_name
		}else if(component.types.includes("locality")){
			form[0].querySelector('[name$="city"]').value = component.long_name
		}else if(component.types.includes("administrative_area_level_1")){
			form[0].querySelector('[name$="state"]').value = component.long_name
		}else if(component.types.includes("postal_code")){
			form[0].querySelector('[name$="zip_code"]').value = component.long_name
		}
	})
    form[0].querySelector('[name$="street_address"]').value = streetAddress
})