<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Garbage Collection Simulator</title>
    <style>
        :root {
            --primary: #2ecc71;
            --secondary: #e74c3c;
            --background: #2c3e50;
            --text: #ecf0f1;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--background);
            color: var(--text);
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #34495e;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
        }

        h1 {
            text-align: center;
            color: var(--primary);
            margin-bottom: 30px;
            font-size: 2.5em;
        }

        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }

        input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 5px;
            background: #43586d;
            color: var(--text);
            font-size: 16px;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s, opacity 0.2s;
        }

        button:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }

        #allocateBtn {
            background: var(--primary);
            color: white;
        }

        #gcBtn {
            background: var(--secondary);
            color: white;
        }

        .memory-status {
            background: #43586d;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }

        .memory-pool {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            min-height: 60px;
            padding: 10px;
            background: #2c3e50;
            border-radius: 5px;
            margin: 15px 0;
        }

        .memory-block {
            padding: 8px 12px;
            border-radius: 4px;
            background: var(--primary);
            color: white;
            font-size: 0.9em;
            animation: appear 0.3s ease;
            transition: transform 0.2s;
        }

        .memory-block:hover {
            transform: scale(1.05);
        }

        .history-log {
            background: #43586d;
            padding: 20px;
            border-radius: 10px;
        }

        #historyEntries {
            max-height: 200px;
            overflow-y: auto;
            margin-top: 10px;
        }

        .log-entry {
            padding: 8px 12px;
            margin: 5px 0;
            background: #2c3e50;
            border-radius: 4px;
            font-size: 0.9em;
            display: flex;
            justify-content: space-between;
            animation: slideIn 0.3s ease;
        }

        .log-entry.allocation {
            border-left: 4px solid var(--primary);
        }

        .log-entry.gc {
            border-left: 4px solid var(--secondary);
        }

        @keyframes appear {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .stats {
            display: flex;
            justify-content: space-between;
            margin: 15px 0;
            padding: 15px;
            background: #43586d;
            border-radius: 8px;
        }

        .stat-item {
            text-align: center;
        }

        .stat-value {
            font-size: 1.2em;
            font-weight: bold;
            color: var(--primary);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🗑️ Garbage Collection Simulator</h1>
        
        <div class="controls">
            <input type="number" id="size" placeholder="Memory size in bytes" min="1">
            <button id="allocateBtn" onclick="allocateMemory()">Allocate Memory</button>
            <button id="gcBtn" onclick="garbageCollect()">Run GC</button>
        </div>

        <div class="memory-status">
            <h2>Memory Status</h2>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-value" id="totalBlocks">0</div>
                    <div>Blocks Allocated</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="totalMemory">0 B</div>
                    <div>Total Memory</div>
                </div>
            </div>
            <div class="memory-pool" id="memoryPool"></div>
        </div>

        <div class="history-log">
            <h2>Operation History</h2>
            <div id="historyEntries"></div>
        </div>
    </div>

    <script>
        let memoryPool = [];
        let allocatedMemory = 0;
        let historyLog = [];

        function allocateMemory() {
            const sizeInput = document.getElementById('size');
            const size = parseInt(sizeInput.value);
            
            if (isNaN(size) || size <= 0) {
                alert("Please enter a valid memory size.");
                return;
            }

            // Add to memory pool
            memoryPool.push(size);
            allocatedMemory += size;
            
            // Add to history
            historyLog.push({
                type: 'allocation',
                size: size,
                timestamp: new Date(),
                totalMemory: allocatedMemory
            });

            updateDisplay();
            sizeInput.value = '';
        }

        function garbageCollect() {
            // Add to history before clearing
            historyLog.push({
                type: 'gc',
                timestamp: new Date(),
                totalMemory: 0
            });

            // Clear memory
            memoryPool = [];
            allocatedMemory = 0;

            updateDisplay();
        }

        function updateDisplay() {
            // Update memory pool display
            const memoryDisplay = document.getElementById('memoryPool');
            memoryDisplay.innerHTML = '';
            memoryPool.forEach((size, index) => {
                const block = document.createElement('div');
                block.className = 'memory-block';
                block.innerText = ${size}B;
                memoryDisplay.appendChild(block);
            });

            // Update stats
            document.getElementById('totalBlocks').textContent = memoryPool.length;
            document.getElementById('totalMemory').textContent = ${allocatedMemory}B;

            // Update history
            const historyDisplay = document.getElementById('historyEntries');
            historyDisplay.innerHTML = '';
            historyLog.slice().reverse().forEach(entry => {
                const logEntry = document.createElement('div');
                logEntry.className = log-entry ${entry.type};
                
                const time = entry.timestamp.toLocaleTimeString();
                const details = entry.type === 'allocation' 
                    ? Allocated ${entry.size}B (Total: ${entry.totalMemory}B)
                    : Garbage Collection performed (Freed ${entry.totalMemory}B);

                logEntry.innerHTML = `
                    <div>${time}</div>
                    <div>${details}</div>
                `;
                
                historyDisplay.appendChild(logEntry);
            });
        }
    </script>
</body>
</html>
