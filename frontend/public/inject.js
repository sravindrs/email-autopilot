// Create a sidebar container
const sidebar = document.createElement('div');
sidebar.id = 'workflow-heatmap-sidebar';
sidebar.style.position = 'fixed';
sidebar.style.top = '0';
sidebar.style.right = '0';
sidebar.style.width = '400px';
sidebar.style.height = '100vh';
sidebar.style.zIndex = '9999';
sidebar.style.background = 'white';
sidebar.style.boxShadow = '0 0 8px rgba(0,0,0,0.2)';
sidebar.style.overflow = 'auto';

// Add to the page
document.body.appendChild(sidebar);

// Inject the React app (built output)
const reactRoot = document.createElement('div');
reactRoot.id = 'root';
sidebar.appendChild(reactRoot);

const script = document.createElement('script');
script.src = chrome.runtime.getURL('assets/index.js'); 
sidebar.appendChild(script);