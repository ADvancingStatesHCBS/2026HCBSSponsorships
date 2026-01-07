// ============================================================
// N8N CODE NODES FOR HCBS SPONSORSHIP WORKFLOW
// ============================================================
// These code blocks replace the 3 separate nodes with 2 optimized ones
// Copy each section into the corresponding n8n Code node

// ============================================================
// CODE NODE 1: "Parse & Combine AI Responses"
// (Replaces "Code in JavaScript" and part of "Isolate Category / Summary")
// ============================================================
// This node parses all batched AI responses and combines them into a single array

const allItems = [];

for (const item of $input.all()) {
  // Get the AI response content
  const content = item.json?.content?.[0]?.text || item.json?.message?.content?.[0]?.text || item.json?.text || '';

  if (!content) continue;

  // Extract JSON from markdown code blocks (```json ... ```)
  const jsonMatch = content.match(/```json\s*([\s\S]*?)\s*```/);

  if (jsonMatch && jsonMatch[1]) {
    try {
      const parsed = JSON.parse(jsonMatch[1].trim());

      // Handle both array and single object responses
      if (Array.isArray(parsed)) {
        allItems.push(...parsed);
      } else {
        allItems.push(parsed);
      }
    } catch (e) {
      // Try parsing the whole content as JSON if no code block found
      try {
        const parsed = JSON.parse(content.trim());
        if (Array.isArray(parsed)) {
          allItems.push(...parsed);
        } else {
          allItems.push(parsed);
        }
      } catch (e2) {
        console.log('Failed to parse JSON:', e2.message);
      }
    }
  }
}

// Return combined data as single item for aggregation
return [{ json: { items: allItems } }];


// ============================================================
// CODE NODE 2: "Normalize for Google Sheets"
// (Replaces "Normalize Data")
// ============================================================
// This node formats the combined data for Google Sheets output

const items = $input.first().json.items || [];
const output = [];

// Aggregate hours by category
const categoryTotals = {};

for (const item of items) {
  const category = item.category || 'Unknown';
  const hours = parseFloat(item.hours) || 0;

  if (!categoryTotals[category]) {
    categoryTotals[category] = 0;
  }
  categoryTotals[category] += hours;
}

// Convert to array format for Google Sheets
for (const [category, hours] of Object.entries(categoryTotals)) {
  output.push({
    json: {
      Category: category,
      Hours: Math.round(hours * 100) / 100  // Round to 2 decimal places
    }
  });
}

// Sort by hours descending
output.sort((a, b) => b.json.Hours - a.json.Hours);

return output;


// ============================================================
// ALTERNATIVE: SINGLE COMBINED NODE
// ============================================================
// If you want to combine everything into ONE code node:

const allData = [];

// Step 1: Parse all AI responses
for (const item of $input.all()) {
  const content = item.json?.content?.[0]?.text || item.json?.message?.content?.[0]?.text || item.json?.text || '';

  if (!content) continue;

  const jsonMatch = content.match(/```json\s*([\s\S]*?)\s*```/);

  if (jsonMatch && jsonMatch[1]) {
    try {
      const parsed = JSON.parse(jsonMatch[1].trim());
      if (Array.isArray(parsed)) {
        allData.push(...parsed);
      } else {
        allData.push(parsed);
      }
    } catch (e) {
      // Skip invalid JSON
    }
  }
}

// Step 2: Aggregate by category
const categoryTotals = {};
for (const item of allData) {
  const category = item.category || 'Unknown';
  const hours = parseFloat(item.hours) || 0;

  if (!categoryTotals[category]) {
    categoryTotals[category] = 0;
  }
  categoryTotals[category] += hours;
}

// Step 3: Format for Google Sheets
const output = Object.entries(categoryTotals)
  .map(([category, hours]) => ({
    json: {
      Category: category,
      Hours: Math.round(hours * 100) / 100
    }
  }))
  .sort((a, b) => b.json.Hours - a.json.Hours);

return output;
