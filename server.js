const express = require('express')
const cors = require('cors')
const fs = require('fs')
const path = require('path')

const app = express()
app.use(cors())
//allows express to read request 
app.use(express.urlencoded({ extended: true }))
app.use(express.json())

//create python file for streamlit and send file to client
app.post('/api/createFile', (req, res) => {
  //iterate through request array and output line by line
  for(var i = 0; i < req.body.data.length; i++){
    fs.appendFile(
      path.join(__dirname, '/files', 'hello.txt'),
      req.body.data[i] + '\r\n',
      err => {
        if(err) throw err
      }
    )
  }
  console.log('Written to file')
  res.send('hello')
})

const port = 5000

app.listen(port, () => console.log(`Server running on port ${port}`))