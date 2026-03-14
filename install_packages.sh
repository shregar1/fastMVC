#!/bin/bash
# Install each FastMVC package in editable mode.
# Uses 'python -m pip' so it works when 'pip' is not on PATH.
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PIP="${PIP:-python -m pip}"
if ! $PIP --version &>/dev/null; then
  PIP="python3 -m pip"
fi

echo "Installing fastmvc_core..."
$PIP install -e ./fastmvc_core

echo "Installing fastmvc_db..."
$PIP install -e ./fastmvc_db

echo "Installing fastmvc_kafka..."
$PIP install -e ./fastmvc_kafka

echo "Installing fastmvc_channels..."
$PIP install -e ./fastmvc_channels

echo "Installing fastmvc_notifications..."
$PIP install -e ./fastmvc_notifications

echo "Installing fastmvc_webrtc..."
$PIP install -e ./fastmvc_webrtc

echo "Installing fastmvc_dashboards..."
$PIP install -e ./fastmvc_dashboards

echo "Installing fastmvc_payments..."
$PIP install -e ./fastmvc_payments

echo "Installing fastmvc_identity..."
$PIP install -e ./fastmvc_identity

echo "Installing fastmvc_queues..."
$PIP install -e ./fastmvc_queues

echo "Installing fastmvc_jobs..."
$PIP install -e ./fastmvc_jobs

echo "Installing fastmvc_storage..."
$PIP install -e ./fastmvc_storage

echo "Installing fastmvc_secrets..."
$PIP install -e ./fastmvc_secrets

echo "Installing fastmvc_feature_flags..."
$PIP install -e ./fastmvc_feature_flags

echo "Installing fastmvc_search..."
$PIP install -e ./fastmvc_search

echo "Installing fastmvc_analytics..."
$PIP install -e ./fastmvc_analytics

echo "Installing fastmvc_llm..."
$PIP install -e ./fastmvc_llm

echo "Installing fastmvc_vectors..."
$PIP install -e ./fastmvc_vectors

echo "Installing fastmvc_tenancy..."
$PIP install -e ./fastmvc_tenancy

echo "Installing fastmvc_admin..."
$PIP install -e ./fastmvc_admin

echo "Installing fastmvc_webhooks..."
$PIP install -e ./fastmvc_webhooks

echo "Installing fastmvc_media..."
$PIP install -e ./fastmvc_media

echo "Installing fast_mvc_main (pyfastmvc)..."
$PIP install -e ./fast_mvc_main

echo "Done. Installed packages:"
$PIP list | grep -iE "fastmvc|pyfastmvc" || true
