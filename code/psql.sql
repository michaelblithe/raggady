-- Enums to match python classes
CREATE TYPE user_type AS ENUM ('PERSONAL', 'BUSINESS', 'ADMIN');
CREATE TYPE access_level AS ENUM ('READ', 'WRITE', 'ADMIN');
CREATE TYPE file_format AS ENUM ('PDF', 'MARKDOWN');
CREATE TYPE metric_type AS ENUM ('COUNT', 'SUM', 'AVG', 'MAX', 'MIN');
CREATE TYPE runtime_type AS ENUM ('PYTHON', 'JAVA', 'GO');

-- User class storage
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    type user_type NOT NULL DEFAULT 'PERSONAL',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DataContainer class storage
create TABLE data_containers(
    container_id UUID PRIMARY KEY,
    owner_user_id UUID NOT NULL REFERENCES users(user_id),
    storage_quota BIGINT NOT NULL,
    used_storage BIGINT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_storage CHECK (used_storage <= storage_quota and storage_quota > 0)
);

-- Implementation of permissions
CREATE TABLE container_permissions(
    permission_id UUID PRIMARY KEY,
    container_id UUID NOT NULL REFERENCES data_containers(container_id),
    user_id UUID NOT NULL REFERENCES users(user_id),
    access_level access_levelNOT NULL DEFAULT 'READ',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(container_id, user_id)
);

-- Documents metadata
CREATE TABLE documents (
    document_id UUID PRIMARY KEY,
    container_id UUID NOT NULL REFERENCES data_containers(container_id),
    filename VARCHAR(255) NOT NULL,
    format file_format NOT NULL,
    size BIGINT NOT NULL,
    s3_key VARCHAR(1024) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    CONSTRAINT positive_size CHECK (size > 0)
);

-- Tools metadata
CREATE TABLE tools (
    tool_id UUID PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    runtime_type runtime_type NOT NULL,
    required_params JSONB NOT NULL, -- Store required_params as JSON for flexibility
    permissions JSONB NOT NULL, -- Store permissions as JSON for flexibility
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);