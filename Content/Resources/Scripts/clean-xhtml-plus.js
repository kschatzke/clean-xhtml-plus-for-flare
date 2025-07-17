/* Open topic popup when user clicks its link */

const cxpTopicPopupLinks = document.querySelectorAll('a[data-cxp-topic-popup-link]');

for (const cxpTopicPopupLink of cxpTopicPopupLinks) {
	cxpTopicPopupLink.addEventListener('click', (event) => {
		const cxpTopicPopupId = cxpTopicPopupLink.getAttribute('data-cxp-topic-popup-link');
		const cxpTopicPopupDialog = 'dialog[data-cxp-topic-popup="' + cxpTopicPopupId + '"]';
		const cxpTopicPopup = document.querySelector(cxpTopicPopupDialog);
		cxpTopicPopup.showModal();
	});
}


/* Close topic popup (dialog) when user clicks outside popup */

const cxpDialogElements = document.querySelectorAll('dialog');

for (const cxpDialogElement of cxpDialogElements) {
	cxpDialogElement.addEventListener('click', (event) => {
		if (event.target == cxpDialogElement) {
			cxpDialogElement.close();
		}
	});
}

/* Show and hide togglers when users click their links */

const cxpTogglerLinks = document.querySelectorAll('a[data-cxp-toggler-link]');

for (const cxpTogglerLink of cxpTogglerLinks) {
	cxpTogglerLink.addEventListener('click', (event) => {
		const cxpTogglerIdString = cxpTogglerLink.getAttribute('data-cxp-toggler-link');
		const cxpTogglerIds = cxpTogglerIdString.split(';');
		for (const cxpTogglerId of cxpTogglerIds) {
			const cxpTogglerAttribute = '[data-cxp-toggler="' + cxpTogglerId + '"]';
			const cxpToggler = document.querySelector(cxpTogglerAttribute);
			if (cxpToggler.style.display === 'block') {
				cxpToggler.style.display = 'none';
				cxpTogglerLink.classList.remove('cxp-toggler-link-open');
			} else {
				cxpToggler.style.display = 'block';
				cxpTogglerLink.classList.add('cxp-toggler-link-open');
			}
		}
	});
}


/* Show and hide drop-down text when user clicks its head link  */

const cxpDropDownHeads = document.querySelectorAll('div[class^="MCDropDownHead"]');

for (const cxpDropDownHead of cxpDropDownHeads) {
	cxpDropDownHead.addEventListener('click', (event) => {
		const cxpDropDownBody = cxpDropDownHead.nextElementSibling;
		if (cxpDropDownBody.style.display === 'block') {
			cxpDropDownBody.style.display = 'none';
			cxpDropDownHead.classList.remove('cxp-drop-down-head-open');
		} else {
			cxpDropDownBody.style.display = 'block';
			cxpDropDownHead.classList.add('cxp-drop-down-head-open');
		}
	});
}


/* Show and hide expanding text when user clicks its head link  */

const cxpExpandingHeads = document.querySelectorAll('span[class^="MCExpandingHead"]');

for (const cxpExpandingHead of cxpExpandingHeads) {
	cxpExpandingHead.addEventListener('click', (event) => {
		const cxpExpandingBody = cxpExpandingHead.nextElementSibling;
		if (cxpExpandingBody.style.display === 'inline') {
			cxpExpandingBody.style.display = 'none';
			cxpExpandingHead.classList.remove('cxp-expanding-head-open');
		} else {
			cxpExpandingBody.style.display = 'inline';
			cxpExpandingHead.classList.add('cxp-expanding-head-open');
		}
	});
}