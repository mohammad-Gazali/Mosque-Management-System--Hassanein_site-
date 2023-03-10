let studentsReportsSearchStudentSection = document.getElementById('search-student-section-students-reports')
let studentsReportsFormSearchStudent = document.querySelector('#search-student-section-students-reports form')
let studentsReportsTitle = studentsReportsSearchStudentSection.closest('h3')
let studentsReportsRadioInputs = document.querySelectorAll('#reports-form-students-reports input[name="type"]')
let studentsReportsSearchInput = document.getElementById('students-reports-search-student')
let studentsReportsHiddenInput = document.querySelector('#reports-form-students-reports input[name="student-id"]')
let studentsReportsDisplayingStudents = document.getElementById('displaying-students-students-reports') 
let studentsReportsDisplayingStudentsFormBody = document.getElementById('div-for-displaying-student-in-form-body-students-reports')
let studentsReportsErrorNotStudentChoosed = document.getElementById('error-section-for-not-choosing-student-students-reports')
let studentsReportsReportsForm = document.getElementById('reports-form-students-reports')
let csrfMiddlewareToken = document.querySelector('#reports-form-students-reports input[name="csrfmiddlewaretoken"]')


Array.from(studentsReportsRadioInputs).forEach((item, index) => {
    item.onchange = () => {
        if (index === 0) {
            studentsReportsSearchStudentSection.classList.add('d-none')
            studentsReportsDisplayingStudentsFormBody.classList.add('d-none')
            studentsReportsReportsForm.onsubmit = (e) => {
                e.target.submit()
            }
        } else {
            studentsReportsSearchStudentSection.classList.remove('d-none')
            studentsReportsDisplayingStudentsFormBody.classList.remove('d-none')
            studentsReportsReportsForm.onsubmit = (e) => {
                e.preventDefault();
                if (!studentsReportsHiddenInput.value) {
                    studentsReportsErrorNotStudentChoosed.innerHTML = ''
                    studentsReportsErrorNotStudentChoosed.className = ''
            
                    studentsReportsErrorNotStudentChoosed.className = 'alert alert-danger'
                    studentsReportsErrorNotStudentChoosed.role = 'alert'
                    studentsReportsErrorNotStudentChoosed.textContent = '?????? ???????????? ???????????? ?????? ?????????? ??????????????'
                } else {
                    e.target.submit();
                }
            }   
        }
    }
})


//* Handling AJAX
const handleFetchEditPoints = async () => {
    const csrfToken = csrfMiddlewareToken.value
    
    const res = await fetch('/json/students', {
        method: "POST",
        mode: 'same-origin',
        headers: {
            "Content-Type":"application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({
            "content": studentsReportsSearchInput.value
        })
    })
    
    const data = await res.json()
    
    return data
}


studentsReportsFormSearchStudent.onsubmit = async (e) => {
    e.preventDefault();
    const data = await handleFetchEditPoints();
    
    studentsReportsDisplayingStudents.innerHTML = ''

    if (data.students.length === 0) {

        const newError = document.createElement('div')
        const textError = document.createTextNode('???? ???????? ???????? ???????? ??????????')
        
        newError.appendChild(textError)
        newError.className = 'alert alert-danger'

        studentsReportsDisplayingStudents.appendChild(newError)

    } else {
        Array.from(data.students).forEach((student) => {
            const newDiv = document.createElement('div')
            const innerButton = document.createElement('button')
            
            const textDiv = document.createTextNode(`[${student.id}] ${student.name}`)
            const textButton = document.createTextNode('????????????')
    
            innerButton.appendChild(textButton)
            innerButton.className = 'btn btn-primary'
            innerButton.dataset.id = student.id
            innerButton.dataset.name = student.name

            newDiv.appendChild(textDiv)
            newDiv.appendChild(innerButton)
            newDiv.className = 'alert alert-primary flex-wrap d-flex gap-3 align-items-center justify-content-between'
            newDiv.id = `student-in-edit-points-form-id-${student.id}`
            newDiv.role = 'alert'

            studentsReportsDisplayingStudents.appendChild(newDiv)
        })

        Array.from(studentsReportsDisplayingStudents.children).forEach((div) => {
            const btn = div.children[0]

            btn.onclick = (e) => {
                studentsReportsDisplayingStudentsFormBody.className = ''
                studentsReportsDisplayingStudentsFormBody.innerHTML = ''

                const stuId = e.target.dataset.id;
                const stuName = e.target.dataset.name;

                const xIcon = document.createElement('i')
                xIcon.className = 'bi bi-x-lg'
                xIcon.style.cursor = 'pointer'

                const textContent = document.createTextNode(`[${stuId}] ${stuName}`)

                studentsReportsHiddenInput.value = stuId;

                studentsReportsDisplayingStudentsFormBody.className = 'alert alert-primary d-flex justify-content-between align-items-center'
                studentsReportsDisplayingStudentsFormBody.appendChild(textContent);
                studentsReportsDisplayingStudentsFormBody.appendChild(xIcon)

                xIcon.onclick = () => {
                    studentsReportsHiddenInput.value = ''
                    studentsReportsDisplayingStudentsFormBody.className = ''
                    studentsReportsDisplayingStudentsFormBody.innerHTML = ''
                }
            }
        })

    }

}