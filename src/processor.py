from datetime import datetime, timedelta
import logging
from uuid import uuid4
from data_model import PipelineItem, PipelineContext, ProtocolizedMessage, Item, ContextElement, Content, Insight, \
    General, Source


def process_json_data(item_id, content_value, source_value, system_time_value):
    """
    Processes JSON data by extracting specific attributes and sending them to the pipeline.

    To send the data to the pipeline topic, the following steps are performed:
    1. Extract "content", "source," and "system_time" attributes from JSON data
    2. Place the "content" (the text) field in the Insight object.
    3. Place the "source" and "system_time" fields in the General object.
    4. Fill in the remaining mandatory fields for the protocolized_message.
    5. Create the protocolized_message object and send it to the pipeline topic


    Example for input JSON file:
    ----------------------------
    {
       "content": "عُمَر مُحَمَّد 🇵🇸\nomar_warda0\n@Salwaosa113 الواد دا ملحد اصلا يعني مش معترف يعني اي شهيد \nولا معترف بكل نصوص القرآن دي اصلا \nهو عايزله صاروخ من بتوع القسام ف دماغه اصلا ..",
       "source": "text_analytics",
       "system_time": 1696957866000
    }
    """

    try:
        current_time = datetime.utcnow()
        start_time = int((current_time - timedelta(hours=1)).timestamp())
        end_time = int(current_time.timestamp())

        general = General(
            end_time=end_time,
            item_id=item_id,
            start_time=start_time,
            sub_type="post_post",
            system_time=system_time_value,
            type="post",
            source_application=source_value
        )

        pipeline_context = PipelineContext(item_id=item_id)

        item_context1 = ContextElement(context_type="COVERAGE", value="683e6f50-81cc-4192-908e-b8f01a4f98e3")
        item_context2 = ContextElement(context_type="ASSET", value="e108d363-968a-4c99-a320-771df7644a96")
        item_context3 = ContextElement(context_type="SUB_INVESTIGATION", value="1da96d05-9b03-41ec-a75f-a3b3061db7aa")
        item_context4 = ContextElement(context_type="INVESTIGATION", value="10bbb0e1-9b1e-4b55-9b56-8bb1845ccd5a")
        item_context5 = ContextElement(context_type="ORGANIZATION_UNIT", value="fa03eb688ad8aa1db593d33dabd89bad")

        item_context_list = [item_context1, item_context2, item_context3, item_context4, item_context5]

        insight_content = Content(value=content_value, ref="")
        insight = Insight(source="text_analytics", content=insight_content, insight_id=1, insight_type="content",
                          tagged_users=[])

        source = Source(model_name="general", raw_data_infos=[])

        # Create the protocolized message
        item = Item(general=general, context=item_context_list, source=source, insights=[insight])
        pipeline_item = PipelineItem(item=item)
        protocolized_message = ProtocolizedMessage(data=pipeline_item, context=pipeline_context)
        return protocolized_message

    except Exception as e:
        raise e
