import {
  CopilotRuntime,
  ExperimentalEmptyAdapter,
  LangGraphHttpAgent,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";
import { NextRequest } from "next/server";
// You can use any service adapter here for multi-agent support.
const serviceAdapter = new ExperimentalEmptyAdapter();
const runtime = new CopilotRuntime({
  agents: {
    'agent': new LangGraphHttpAgent({url: "http://localhost:8000/agent"}),  },
});
export const POST = async (req: NextRequest) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: "/api/copilot",
  });
  return handleRequest(req);
};