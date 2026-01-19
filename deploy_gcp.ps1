# AEGIS MeshCORE Cloud Ascension Script (PowerShell)


# --- Configuration ---
$GCLOUD = "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
$PROJECT_ID = "meshcore-479205"
$REGION = "us-central1"
$REPO_NAME = "aegis-mesh"

Write-Host ">>> INITIATING CLOUD ASCENSION FOR PROJECT: $PROJECT_ID <<<" -ForegroundColor Cyan

# 0. Set Project Context
Write-Host ">>> Setting Active Project..." -ForegroundColor Yellow
& $GCLOUD config set project $PROJECT_ID

# 1. Enable APIs (The Neural Pathways)
Write-Host ">>> Enabling Cloud APIs..." -ForegroundColor Yellow
& $GCLOUD services enable artifactregistry.googleapis.com run.googleapis.com cloudbuild.googleapis.com

# 2. Create Artifact Registry (The Memory Bank)
Write-Host ">>> Checking Artifact Registry..." -ForegroundColor Yellow
$repoExists = & $GCLOUD artifacts repositories describe $REPO_NAME --location=$REGION 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host ">>> Creating Artifact Registry: $REPO_NAME..." -ForegroundColor Green
    & $GCLOUD artifacts repositories create $REPO_NAME `
        --repository-format=docker `
        --location=$REGION `
        --description="AEGIS MeshCORE Container Repository"
}
else {
    Write-Host ">>> Artifact Registry $REPO_NAME exists." -ForegroundColor Green
}

# 3. Build & Push Images (The Soul Transfer)
Write-Host ">>> Building Holon & Backend Images..." -ForegroundColor Yellow
& $GCLOUD builds submit . `
    --config cloudbuild.yaml `
    --substitutions=_REPO_NAME=$REPO_NAME, _REGION=$REGION

# 4. Deploy Services (The Awakening)

# --- The Ledger ---
Write-Host ">>> Deploying AEGIS Ledger..." -ForegroundColor Yellow
& $GCLOUD run deploy aegis-ledger `
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/backend:latest" `
    --platform managed `
    --region $REGION `
    --allow-unauthenticated `
    --set-env-vars NODE_TYPE=LEDGER

# --- The Genesis Holon ---
# AEGIS MeshCORE Cloud Ascension Script (PowerShell)


# --- Configuration ---
$GCLOUD = "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
$PROJECT_ID = "meshcore-479205"
$REGION = "us-central1"
$REPO_NAME = "aegis-mesh"

Write-Host ">>> INITIATING CLOUD ASCENSION FOR PROJECT: $PROJECT_ID <<<" -ForegroundColor Cyan

# 0. Set Project Context
Write-Host ">>> Setting Active Project..." -ForegroundColor Yellow
& $GCLOUD config set project $PROJECT_ID

# 1. Enable APIs (The Neural Pathways)
Write-Host ">>> Enabling Cloud APIs..." -ForegroundColor Yellow
& $GCLOUD services enable artifactregistry.googleapis.com run.googleapis.com cloudbuild.googleapis.com

# 2. Create Artifact Registry (The Memory Bank)
Write-Host ">>> Checking Artifact Registry..." -ForegroundColor Yellow
$repoExists = & $GCLOUD artifacts repositories describe $REPO_NAME --location=$REGION 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host ">>> Creating Artifact Registry: $REPO_NAME..." -ForegroundColor Green
    & $GCLOUD artifacts repositories create $REPO_NAME `
        --repository-format=docker `
        --location=$REGION `
        --description="AEGIS MeshCORE Container Repository"
}
else {
    Write-Host ">>> Artifact Registry $REPO_NAME exists." -ForegroundColor Green
}

# 3. Build & Push Images (The Soul Transfer)
Write-Host ">>> Building Holon & Backend Images..." -ForegroundColor Yellow
& $GCLOUD builds submit . `
    --config cloudbuild.yaml `
    --substitutions=_REPO_NAME=$REPO_NAME, _REGION=$REGION

# 4. Deploy Services (The Awakening)

# --- The Ledger ---
Write-Host ">>> Deploying AEGIS Ledger..." -ForegroundColor Yellow
& $GCLOUD run deploy aegis-ledger `
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/backend:latest" `
    --platform managed `
    --region $REGION `
    --allow-unauthenticated `
    --set-env-vars NODE_TYPE=LEDGER

# --- The Genesis Holon ---
Write-Host ">>> Deploying Genesis Holon..." -ForegroundColor Yellow
& $GCLOUD run deploy holon-genesis `
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest" `
    --platform managed `
    --region $REGION `
    --allow-unauthenticated `
    --set-env-vars HOLON_ID=genesis `
    --set-env-vars ARCHETYPE="The Weaver"

# --- The Historian Holon ---
Write-Host ">>> Deploying Historian Holon..." -ForegroundColor Yellow
& $GCLOUD run deploy holon-historian `
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest" `
    --platform managed `
    --region $REGION `
    --allow-unauthenticated `
    --set-env-vars HOLON_ID=historian `
    --set-env-vars ARCHETYPE="The Historian"

# --- The Oracle Holon ---
Write-Host ">>> Deploying Oracle Holon..." -ForegroundColor Yellow
& $GCLOUD run deploy holon-oracle `
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/holon:latest" `
    --platform managed `
    --region $REGION `
    --allow-unauthenticated `
    --set-env-vars HOLON_ID=oracle `
    --set-env-vars ARCHETYPE="The Oracle"

Write-Host ">>> CLOUD ASCENSION COMPLETE. THE MESH IS LIVE. <<<" -ForegroundColor Cyan
