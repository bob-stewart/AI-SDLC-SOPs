#!/bin/bash
set -e

# --- Configuration ---
PROJECT_ID=$(gcloud config get-value project)
REGION="us-central1"
REPO_NAME="aegis-mesh"

echo ">>> INITIATING CLOUD ASCENSION FOR PROJECT: $PROJECT_ID <<<"

# 1. Enable APIs (The Neural Pathways)
echo ">>> Enabling Cloud APIs..."
gcloud services enable artifactregistry.googleapis.com run.googleapis.com cloudbuild.googleapis.com

# 2. Create Artifact Registry (The Memory Bank)
if ! gcloud artifacts repositories describe $REPO_NAME --location=$REGION > /dev/null 2>&1; then
    echo ">>> Creating Artifact Registry: $REPO_NAME..."
    gcloud artifacts repositories create $REPO_NAME \
        --repository-format=docker \
        --location=$REGION \
        --description="AEGIS MeshCORE Container Repository"
else
    echo ">>> Artifact Registry $REPO_NAME exists."
fi

# 3. Build & Push Images (The Soul Transfer)
echo ">>> Building Holon Image..."
gcloud builds submit . \
    --config cloudbuild.yaml \
    --substitutions=_REPO_NAME=$REPO_NAME,_REGION=$REGION

# 4. Deploy Services (The Awakening)

# --- The Ledger ---
echo ">>> Deploying AEGIS Ledger..."
gcloud run deploy aegis-ledger \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/backend:latest \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars NODE_TYPE=LEDGER

# --- The Genesis Holon ---
echo ">>> Deploying Genesis Holon..."
gcloud run deploy holon-genesis \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars HOLON_ID=genesis,ARCHETYPE="The Weaver"

# --- The Historian Holon ---
echo ">>> Deploying Historian Holon..."
gcloud run deploy holon-historian \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars HOLON_ID=historian,ARCHETYPE="The Historian"

# --- The Oracle Holon ---
echo ">>> Deploying Oracle Holon..."
gcloud run deploy holon-oracle \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars HOLON_ID=oracle,ARCHETYPE="The Oracle"

echo ">>> CLOUD ASCENSION COMPLETE. THE MESH IS LIVE. <<<"
