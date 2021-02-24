import axios from 'axios'

function FileCreator(){
    //post request to nodejs server to create a python file for streamlit
    const data = [0, 1, 2]
    function filePost(){
        axios.post("http://localhost:5000/api/createFile", {data})
            .then(res => {
                console.log(res)
            })
    }
    return(
        <>
            <button onClick = {filePost}>Post!</button>
        </>
    )
}

export default FileCreator