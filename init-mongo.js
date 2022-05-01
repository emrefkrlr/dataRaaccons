db.createUser({
    user: "emrefikirlier",
    pwd: "1234",
    roles: [{
        role: "readWrite",
        db: "dataRaccoons"

    }]
})