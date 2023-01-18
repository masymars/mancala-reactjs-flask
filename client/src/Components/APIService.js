export default class APIService{
    // Insert an article
    static move_player(body){
        return fetch(`http://localhost:5000/do`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
    static move_comp(){
        return fetch(`http://localhost:5000/doc`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify("1")
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
    static getbord(){
        return fetch(`http://localhost:5000/getbord`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify("1")
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}