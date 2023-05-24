# Python ETL Toolkit


## Project Architecture
In Clean Architecture, the layers can be ordered by their dependencies, with the inner layers depending on the outer layers. Here's the ordered list along with a description of each layer:

![clean architecture diagram](https://sunscrapers.com/images/blog/CleanArchitecture.webp)

### Entities (Domain Model):

The Entities layer represents the core business logic and domain-specific concepts of the application.
It contains the essential entities, their attributes, relationships, and behavior.
Entities encapsulate the business rules, calculations, and constraints of the domain.
This layer is independent of any external systems or frameworks, ensuring a high level of reusability and testability.

### Repositories (Data Access):

The Repositories layer is responsible for data access and persistence.
It provides an interface to interact with the data storage, such as databases or external services.
Repositories encapsulate the details of data storage and retrieval, including queries, transactions, and caching.
This layer implements the interfaces defined by the Entities layer to store and retrieve data while maintaining data integrity.

 ### Use Cases (Business Logic):

The Use Cases layer contains the application's core business logic and orchestrates the interactions between the Entities and Repositories layers.
Use Cases represent the specific operations and workflows of the application.
They enforce the business rules and handle the coordination of entities and data access operations.
This layer is independent of the external interfaces and frameworks, ensuring testability and maintainability.

### API Layer (Frameworks & Drivers):

The API Layer, also known as the Interface Adapters layer, provides the communication interface between the application and external systems.
It includes the implementation of API endpoints, request handling, and response formatting.
The API layer interacts with the Use Cases layer to execute the application's business logic and process requests.
This layer is responsible for adapting the external systems' inputs and outputs to the application's internal structures.

### Presentation (UI & Controllers):

The Presentation layer handles the user interface and user interaction aspects of the application.
It includes the implementation of user interfaces, such as web pages, mobile app screens, or command-line interfaces.
The Presentation layer interacts with the API layer to send requests, receive responses, and present information to users.
This layer focuses on the rendering and display of data and capturing user input.
It's important to note that the dependencies flow inward, with each layer depending on the layers closer to the outer edge. The inner layers contain the core business logic and domain-specific rules, while the outer layers deal with the interaction with external systems and interfaces.

This layering approach provides several benefits, such as maintainability, testability, and flexibility, by enforcing a separation of concerns and allowing each layer to be developed and modified independently.

---

## Potential Use Cases
- Upload file to S3
- Extract and read file from S3
- Add data from csv to Sql Server
- Query Sql Server
- Process data in sql server