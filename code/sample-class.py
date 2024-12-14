from enum import Enum
from datetime import date

class MetricType(Enum):
    """The type of metric to be measured."""
    COUNT = 1
    SUM = 2
    AVG = 3
    MAX = 4
    MIN = 5

class Metric:
    """A metric that can be used to KPIs and performance data."""
    type: MetricType
    value: float
    timestamp: date

class MetricRepository:
    """Stores and retrieves metrics"""
    def save_metric(metric: Metric)-> None:
        """Save a single metric"""
        pass

    def get_metrics_by_type(metric_type: MetricType) -> list[Metric]:
        """Get all the metrics by type"""
        pass

class TimeRange:
    """A time range for a metric search"""
    start: date
    stop: date

class MetricReport:
    """A report of system metrics"""
    metrics: list[Metric]
    time_range: TimeRange

class MetricsController:
    """Controls the retrieval and processing of system metrics."""
    metrics_repository: MetricRepository
    def get_system_metrics(timeRange: TimeRange) -> MetricReport:
       """Get system metrics for a given time range."""
       pass

class AuthRequest:
    """A request to authenticate a user."""
    username: str
    password: str

class AuthToken:
    """A token used to authenticate a user."""
    token: str

class User:
    """ A record of a user """
    user_id: str
    email: str
    name: str

class AuthProvider:
    """A provider for authentication."""
    def validate_token(token: str) -> User:
        """Validate an authentication token and return the user information"""
        pass
    def authenticate(credentials: AuthRequest) -> AuthToken:
        """Authenticate a user and return an authentication token"""
        pass

class AccessLevel(Enum):
    """How much access a user has for a data container"""
    READ = 1
    WRITE = 2
    ADMIN = 3

class AccessController:
    """An entrypoint for managing user access"""
    auth_provider: AuthProvider 
    def grand_access(containerId: str, userId: str, level: AccessLevel) -> None: 
        """Grant access to a data container for a user."""
        pass

class SearchResult: 
    """ Class which represents a single search result. """
    relevence_score: float 
    document_refs: list[str]


class FileFormat(Enum):
    """The format of a document."""
    PDF = 1
    MARKDOWN = 2

class Document:
    """A document entry"""
    document_id: str 
    format: FileFormat
    size: int
    content: bytearray

class Embedding:
    """The embedding form of the document"""
    vector_data: list[list[float]]
    timetsamp: date
    document_ref: str


class DataContainer: 
    """Acontainer for data, with a set of documents and a storage quota."""
    container_id: str
    storage_quoat: int
    used_storage: int


class StorageProvider:
    """A provider for storing and retrieving documents."""
    def store_file(file: Document) -> None:
        """Stores a file to storage."""
        pass 
    def retrieve_file(path: str) -> Document:
        """Retrieves a file from storage."""
        pass

class GenAIGateway:
    """A gateway for interacting with generative AI models."""
    def generate_embedding(text: str) -> Embedding:
        """Generates an embedding for a given text."""
        pass

    def invoke_with_context(prompt: str, context: str) ->str:
        """Invokes a generative AI model with a given prompt and context."""
        pass

class RuntimeType(Enum):
    """The type of environment to run the tool in"""
    PYTHON = 1
    JAVA = 2
    GO = 3

class ToolInvocationResult:
    """The results of a tool invocation"""
    tool_logs: str
    output: map[str, any]

class Tool:
    """A tool entrypoint for interacting with a tool."""
    runtime_type: RuntimeType
    name: str
    required_params: list[str]
    permissions: list[str]

    def invoke(params: map) -> ToolInvocationResult:
        """Invokes a tool with a given set of parameters."""
        pass

class ToolRepository:
    """A repository for tools"""
    def get_tool(toolName:str) -> Tool:
        """Gets a tool by name."""
        pass

class ToolController:
    tool_repository: ToolRepository
    genAIGateway: GenAIGateway
    def invoke_tool(toolName:str, params: map) -> ToolInvocationResult:
        pass


class DocumentRepository:
    def save(document: Document) -> None:
        pass
    def findBy(id: str) -> Document:
        pass
    def delete(id: str) -> None:
        pass

class EmbeddingRepository:
    """A repository for embeddings"""
    def save_embeddings(doc_id: str, embeddings: list[Embedding]) -> None:
        """Saves embeddings for a given document."""
        pass
    def find_similar(embedding: Embedding) -> list[Embedding]:
        """Finds similar embeddings."""
        pass

class SearchController:
    """The controller for handling search requests."""
    document_repository: DocumentRepository
    embedding_repository: EmbeddingRepository
    genAIGateway: GenAIGateway

    def perform_search(query: str, container_id: str) -> list[SearchResult]:
        """Performs a search for documents."""
        pass

class DocumentController:
    """The controller for handling document requests."""
    document_repository: DocumentRepository
    storage_provider: StorageProvider
    genAIGateway: GenAIGateway

    def upload_document(file: bytearray, container_id: str) -> None:
        """Uploads a document to storage."""
        pass

    def delete_document(document_id: str) -> None:
        """Deletes a document from storage."""
        pass

